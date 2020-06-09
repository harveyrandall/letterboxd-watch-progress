# Implemented with reference to:
# https://devcenter.heroku.com/articles/clock-processes-python
from apscheduler.schedulers.background import BlockingScheduler
from letterboxd import get_diary

scheduler = BlockingScheduler()
scheduler.add_job(get_diary, 'cron', day="*", hour=5)

scheduler.start()