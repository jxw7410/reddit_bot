import config as cfg

from lurker_bot import LurkerBotBeta

subreddit = 'personalspacefordev'

bot = LurkerBotBeta(cfg.reddit, subreddit)

bot.run()
