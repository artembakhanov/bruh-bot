from sqlalchemy.sql import ClauseElement

from db.classes import Session, User


def db_read(function):
    """
    Wrapper that is used when one needs to read something from the database
    :param function: function where the operation is performed
    :return: the wrapper
    """

    def wrapper(*args, **kwargs):
        session = Session()
        ret = function(session, *args, **kwargs)
        session.close()
        return ret

    return wrapper


def db_write(function):
    """
    Wrapper that is used when one needs to read/write something from/to the database
    :param function: function where the operation is performed
    :return: the wrapper
    """

    def wrapper(*args, **kwargs):
        session = Session()
        ret = function(session, *args, **kwargs)
        session.commit()
        session.close()
        return ret

    return wrapper


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance, True


def create_user(function):
    def wrapper(*args, **kwargs):
        session = Session()
        user = args[0].from_user
        not_registered = get_or_create(session, User, id=user.id)[1]
        session.commit()
        session.close()
        ret = function(not_registered, *args, **kwargs)
        return ret

    return wrapper
