import flask  # pip3 install flask
from pywa import WhatsApp
from pywa.types import Message
import os

flask_app = flask.Flask(__name__)

wa = WhatsApp(
    phone_id=os.environ["PHONE_ID"],
    token=os.environ["AUTH_TOKEN_PERMENANT_META"],
    server=flask_app,
    webhook_endpoint="/webhook",
    verify_token=os.environ["VERIFY_TOKEN"],
    # callback_url=os.environ["NGROK_DOMAIN_URL"],
    # app_id=os.environ["APP_ID"],
    # app_secret=os.environ["APP_SECRET"],
)


@wa.on_message()
def hello(_: WhatsApp, msg: Message):
    msg.react("👋")
    msg.reply(f"Hello {msg.from_user.name}!")


# Run the server
if __name__ == "__main__":
    # start the server with flask or gunicorn, waitress, etc.
    flask_app.run()
