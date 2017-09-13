import praw
from config.local import client_id, client_secret, user_agent

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)
for submission in reddit.subreddit('cats').hot(limit=3):
    print(submission.url)
    i = 42
