# Implemented with reference to:
# https://devcenter.heroku.com/articles/clock-processes-python
from apscheduler.schedulers.background import BlockingScheduler
import letterboxd

scheduler = BlockingScheduler()

@scheduler('cron', hour=5)
def update_diary():
    letterboxd.get_diary()

scheduler.start()