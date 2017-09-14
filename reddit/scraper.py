import praw

from config.local import reddit_secrets

_reddit = None


def _connect():
    global _reddit
    _reddit = praw.Reddit(**reddit_secrets.__dict__)


def cats(amount):
    if not _reddit:
        _connect()
    subs = _reddit.subreddit('cats').hot(limit=amount)
    return map(lambda s: s.url, subs)
