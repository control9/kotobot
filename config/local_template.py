from config.secrets import RedditSecrets, TelegramSecrets

reddit_secrets = RedditSecrets(
    client_id='ID',
    client_secret='verysecret',
    user_agent='somereasonableuseragent',
)

telegram_secrets = TelegramSecrets(token='123456789:SECURETOKEN')
channel_id = '-100123456789'
