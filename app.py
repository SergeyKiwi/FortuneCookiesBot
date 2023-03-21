from flask import Flask
from flask import request
from flask import Response
import requests

from FortuneCookiesBot.credentials import BOT_TOKEN, URL
from FortuneCookiesBot.webhook import set_webhook_url
from FortuneCookiesBot.predictionmanagerfile import PredictionManagerFile

TOKEN = BOT_TOKEN
WEBHOOK_URL_EMPTY = "https://api.telegram.org/bot{token}/setWebhook?url={url_ngrok}"
WEBHOOK_URL = WEBHOOK_URL_EMPTY.format(token=BOT_TOKEN, url_ngrok=URL)

# Set webhook url in Telegram API
status_webhook = set_webhook_url(WEBHOOK_URL)

# Create Flask app
app = Flask(__name__)

#Create predictions manager
predictionManager = PredictionManagerFile()


def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    user = message['message']['from']
    first_name = user.get('first_name')
    last_name = user.get('last_name')

    username = None

    if first_name is not None:
        username = first_name

    if last_name is not None:
        username += " " + last_name

    if first_name is None and last_name is None:
        username = "stranger"

    return chat_id, txt, username


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def get_response(text, username):
    response = None
    if text == '/start':
        response = "Welcome, {}!".format(username)
    elif text == "/get":
        response = predictionManager.get_prediction()
        response = 'Preditction for you, {}\n\n"{}"'.format(username, response)
    else:
        response = "Don't understand now!"
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        print(msg)

        chat_id, txt, username = parse_message(msg)

        response = get_response(txt, username)

        tel_send_message(chat_id, response)

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    if status_webhook:
        app.run(debug=True)
    else:
        print("The application is stopped. Error Telegram Webhook!")
