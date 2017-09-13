import praw

from config.local import client_id, client_secret, user_agent

_reddit = None


def _connect():
    global _reddit
    _reddit = praw.Reddit(client_id=client_id,
                          client_secret=client_secret,
                          user_agent=user_agent)


def cats(amount):
    if not _reddit:
        _connect()
    subs = _reddit.subreddit('cats').hot(limit=amount)
    return map(lambda s: s.url, subs)
