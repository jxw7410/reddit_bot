import praw

class LurkerBotBeta:
  BOT_NAME = 'lurker-bot-beta'
  USER_AGENT = 'lurker-bot-beta v.0.0.1'

  def __init__(self, config, subreddit_name):
    print(config)
    self.reddit = praw.Reddit(client_id=config['client_id'],
                              client_secret=config['client_secret'],
                              username=config['username'],
                              password=config['password'],
                              user_agent=config['user_agent'])

    self.subreddit_name = subreddit_name

  def run(self):
    print(self.USER_AGENT)

  def get_submissions(self): 
    for submission in self.reddit.subreddit(self.subreddit_name).new(limit=25):
      print(submission)
  

  # For credential testing
  def is_logged_in(self):
    print(f'{self.reddit.user.me()} is logged in')
