import config as cfg

from lurker_bot import LurkerBotBeta

subreddit = 'all'

bot = LurkerBotBeta(cfg.reddit, subreddit)

bot.get_submissions()
