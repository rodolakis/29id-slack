import os
import pathlib
from slack_bolt import App
from dotenv import load_dotenv
import pv

# Set bot token and signing secret as environment values
env_path = os.path.join(str(pathlib.Path.home()), '.env')
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

@app.message("user")
def handle_message_user(body, say, logger):
    logger.info(body)
    s_pvs = slack_pvs("2bma:TomoScan:", "2bmbSP1:HDF1:")
    text = s_pvs['user_name'].get()
    # s_pvs['user_last_name'].get()
    # s_pvs['user_affiliation'].get()
    # s_pvs['user_email'].get()
    # s_pvs['user_badge'].get()

    # s_pvs['proposal_number'].get()
    # s_pvs['proposal_title'].get()

    # s_pvs['FPNumCaptured'].get()
    # s_pvs['FPFullFileName'].get() 
    say(text)

@app.event("message")
def handle_message_events(body, say, logger):
    logger.info(body)
    say('Do not know what to do')


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))