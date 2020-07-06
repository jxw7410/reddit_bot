import praw
import time

from services.SiteRegex import SiteRegex
from services.SubParser import SubParser

class LurkerBotBeta:
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
      
    self.stream_submissions()

  def stream_submissions(self):
    subReddit = self.reddit.subreddit(self.subreddit_name)
    
    for submission in subReddit.stream.submissions():
      if submission.clicked: 
        continue 
      
      self.process_url(submission)

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
