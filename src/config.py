import os
from dotenv import load_dotenv

load_dotenv()

reddit = {
    "client_id": os.environ['REDDIT_LURKER_BOT_ID'],
    "client_secret": os.environ['REDDIT_LURKER_BOT_SECRET'],
    "username": os.environ['USERNAME'],
    "password": '',
    "user_agent": f'lurker application v0.0.1 for /u/{ os.environ["USERNAME"] }'
}
