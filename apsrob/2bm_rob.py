import os
import pathlib
from dotenv import load_dotenv
from slack_sdk import WebClient 
from slack_bolt import App 
from slack_bolt.adapter.socket_mode import SocketModeHandler 

# Set bot tokens as environment values
env_path = os.path.join(str(pathlib.Path.home()), '.env')
load_dotenv(dotenv_path=env_path)

bot_token = os.environ.get("BOT_TOKEN")
app_token = os.environ.get("APP_TOKEN") 

def text_match(txt_src, txt_tgt): 
    if txt_tgt[:len(txt_src)].lower()==txt_src.lower(): 
        return True 
    else: 
        return False 

app = App(token = bot_token)

@app.event("message") 
def reply(payload, say, client): 
    try: 
        text = payload["text"] 
    except: 
        return 
    user = client.users_info(user=payload["user"])["user"]["real_name"] 
    chan = client.conversations_info(channel=payload["channel"])["channel"]["name"]

    if chan == "2-bm": 
        if text_match(text, "status"): 
            say("2-BM status is: ....")
        elif text_match(text, "scan"): 
            say("2-BM scan: ....")
        else:
            say("No answer for this ...") 
    elif chan == "automated": 
    # elif chan == "7-bm": 
        if text_match(text, "status"): 
            say("7-BM status is: ....")
        elif text_match(text, "scan"): 
            say("7-BM scan: ....")
        else:
            say("7-BM No answer for this ...") 
    else:
        if text_match(text, "hello"):
            say("Greetings *{0}*!".format(user)) 


if __name__ == "__main__": 
    SocketModeHandler(app, app_token).start() 
