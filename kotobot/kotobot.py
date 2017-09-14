import logging

from telegram import Bot
from config.local import telegram_secrets

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

bot = Bot(telegram_secrets.token)
