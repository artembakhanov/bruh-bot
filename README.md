# BruhBot

This is simple telegram bot that can send bruh sounds. 
Original bot can be found [here](https://t.me/br_uh_bot).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For running this project you need to install Python 3.6 or higher. <br>
In Ubuntu, Mint and Debian you can install Python like this:
```shell script
sudo apt-get install python3 python3-pip
```
You might also need a DBMS such as PostgreSQL or MySQL.

### Installing
1. Clone the repo
```shell script
git clone https://github.com/artembakhanov/bruh-bot.git
```
2. Change the directory
```shell script
cd bruh-bot
```
3. Install dependencies
```shell script
sudo pip3 install -r requirements.txt
```
4. Set config parameters (they are used if environment variables are not set).
```python
TOKEN = "<your_bot_token>"
DATABASE_URL = "sqlite:///hello.db"
```
5. Run `main.py`
```shell script
python3 main.py
```

## Deployment on Heroku

If you want to deploy this project on [Heroku](https://heroku.com), follow these instructions.
1.  Create app
```shell script
heroku create
```
2. Set enviroment variables
```shell script
  heroku config:set DATABASE_URL=<database_url>
  heroku config:set t_token=<your_bot_token>
```
   If you want the bot to work on webhooks, add the following variables
```shell script
  heroku config:set webhooks=<database_url>
  heroku config:set APP_URL=<your_heroku_app_url>
```
3. Deploy the code
```shell script
git push heroku master
```
4. (Optional) If the bot is working on webhooks open you app in browser.

## Built With

* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - Python API wrapper
* [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/yourFeature`)
3. Commit your Changes (`git commit -m 'Add some yourFeature'`)
4. Push to the Branch (`git push origin feature/yourFeature`)
5. Open a Pull Request

## Authors

* **Artem Bakhanov** - [@artembakhanov](https://github.com/artembakhanov)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Memes are the best

