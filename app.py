from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('KkIIUDSiGrMEoeUi+iRiZNfY5Gce7zyINhGfZbR0ln+VcCZTDRg3E01IlU5QuERIQ7SABUzH/J6G7ReeCFlgM0xQG388iOrY4e5WKZ6m2rOR/6Twg8NeCnD894e5WKZ6m2rOR/6Twg8NeCnD894E5WKZ6m2rOR/6Twg8NeCnD89')
handler = WebhookHandler('15f798f915c02f0859c39798570a61bf')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
