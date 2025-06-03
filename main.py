from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if not data or data.get("auth_token") != AUTH_TOKEN:
        return {"status": "unauthorized"}, 401

    message = data.get("message")
    if message:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
        return {"status": "sent"}, 200

    return {"status": "no message"}, 400

if __name__ == "__main__":
    app.run(port=8000)
