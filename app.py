from flask import Flask, request
import telegram
from FortuneCookiesBot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), method=['POST'])
def respond():
    pass