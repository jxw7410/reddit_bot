import praw
import time

from services.SiteRegex import SiteRegex
from services.SubParser import SubParser

class LurkerBotBeta:
  BOT_NAME = 'lurker-bot-beta'
  USER_AGENT = 'lurker-bot-beta v.0.0.1'

  def __init__(self, config, subreddit_name):
    self.reddit = praw.Reddit(client_id=config['client_id'],
                              client_secret=config['client_secret'],
                              username=config['username'],
                              password=config['password'],
                              user_agent=config['user_agent'])

    self.config = config
    self.subreddit_name = subreddit_name
    self.prev_post_ids = []


  def run(self):
    if self.is_logged_in() is None: 
      return

    while True:
      self.check_new_submissions()
      time.sleep(2)


  def check_new_submissions(self): 
      submissions = self.get_submissions()
      new_submission_ids = self.get_submission_ids(submissions)
      diff_ids = self.get_different_ids(new_submission_ids)

      if len(diff_ids) and diff_ids != self.prev_post_ids:
        for submission in self.filter_new_submissions(diff_ids, submissions):
          self.process_url(submission)

        self.prev_post_ids = new_submission_ids
      else: 
        print('no changes in id')
  

  def get_submissions(self): 
    return list(self.reddit.subreddit(self.subreddit_name).new(limit=25))


  def get_submission_ids(self, submissions):
    return list(map(lambda submission: submission.id, submissions))


  def get_different_ids(self, new_submission_ids):
    return list(set(new_submission_ids) - set(self.prev_post_ids))


  def filter_new_submissions(self, diff_ids, submissions):
    return list(filter(lambda submission: submission.id in diff_ids, submissions))


  def process_url(self, submission):
    if SiteRegex.is_amazon_product_url(submission.url): 
        if self.is_posted(submission): 
          return

        submission.reply('Beep Boop This is the lurker bot. I noticed you posted an amazon url. Please do not reply.')

    
  def is_posted(self, submission):
    top_level_comments = list(submission.comments)
    comment_authors = list(map(lambda sub: sub.author, top_level_comments))
    
    return self.config['username'] in comment_authors

  def is_logged_in(self):
    try:
      return self.reddit.user.me()
    except: 
      return None
