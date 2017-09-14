from time import sleep

from reddit import scraper
from kotobot.kotobot import bot
from config.local import channel_id

urls = scraper.cats(3)

for url in urls:
    bot.send_photo(channel_id, url)
    sleep(3)
