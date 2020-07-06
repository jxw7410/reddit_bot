import praw
import time

class LurkerBotBeta:
  BOT_NAME = 'lurker-bot-beta'
  USER_AGENT = 'lurker-bot-beta v.0.0.1'

  def __init__(self, config, subreddit_name):
    self.reddit = praw.Reddit(client_id=config['client_id'],
                              client_secret=config['client_secret'],
                              username=config['username'],
                              password=config['password'],
                              user_agent=config['user_agent'])

    self.subreddit_name = subreddit_name
    self.prev_post_ids = []

  def run(self):
    while True:
      self.get_submissions()
      time.sleep(2)

  def get_submissions(self): 
      submissions = self.reddit.subreddit(self.subreddit_name).new(limit=25)
      diff_ids = self.get_different_ids(self.get_submission_ids(submissions))

      if diff_ids != self.prev_post_ids:
        print(diff_ids)
        self.prev_post_ids = diff_ids
      else: 
        print('no changes in id')
  

  def get_submission_ids(self, submissions):
    return list(map(lambda submission: submission.id, submissions))

  def get_different_ids(self, new_submission_ids):
    return list(set(self.prev_post_ids) - set(new_submission_ids))

  # For credential testing
  def is_logged_in(self):
    print(f'{self.reddit.user.me()} is logged in')
