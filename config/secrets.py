class RedditSecrets:
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent


class TelegramSecrets:
    def __init__(self, token):
        self.token = token
