
import os
from pathlib import Path
from slack_bolt import App
from dotenv import load_dotenv

# Set bot token and signing secret as environment values
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET"),
)

# Listens to incoming messages that contain "hello"
@app.message("hello")
def handle_message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
            }
        ],
        text=f"Hey there <@{message['user']}>!",
    )

# Listens to incoming messages that contain "hello"
@app.message("current")
def handle_message_current(body, say, logger):
    logger.info(body)
    say('curent is 100 mA')   

@app.message("user")
def handle_message_user(body, say, logger):
    logger.info(body)
    say('Today user is')

@app.event("message")
def handle_message_events(body, say, logger):
    logger.info(body)
    say('Do not know what to do')




# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))