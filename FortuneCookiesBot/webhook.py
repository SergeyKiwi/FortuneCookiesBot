import requests

from FortuneCookiesBot.credentials import WEBHOOK_URL_EMPTY, BOT_TOKEN, URL

WEBHOOK_URL = WEBHOOK_URL_EMPTY.format(token=BOT_TOKEN, url_ngrok=URL)


def set_webhook_url(webhook_url):
    req = requests.get(webhook_url)

    if req.status_code == 200:
        req_json = req.json()
        print("Ngrok message: ", req_json)

        if req_json["result"]:
            return True
    else:
        return False


if __name__ == "__main__":
    status = set_webhook_url()
    print(status)
