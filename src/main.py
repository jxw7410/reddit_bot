import config as cfg
from LurkerBot import LurkerBotBeta

def main():
  subreddit = 'personalspacefordev'
  
  bot = LurkerBotBeta(cfg.reddit, subreddit)
  bot.run()

if __name__ == '__main__':
  main()
