# Implemented with reference to:
# https://devcenter.heroku.com/articles/clock-processes-python
from apscheduler.schedulers.blocking import BlockingScheduler
from letterboxd import get_diary
from utils import cronjob

scheduler = BlockingScheduler()
scheduler.add_job(get_diary, 'interval', hours=1)
scheduler.add_job(cronjob, 'interval', seconds=10)

scheduler.start()