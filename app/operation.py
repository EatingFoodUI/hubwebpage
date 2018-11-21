# -*- coding: utf-8 -*
# from xx import use_fun()
import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# 七天执行一次
# @sched.scheduled_job('interval', days=7)

# 在每个月的星期五8：00执行
@sched.scheduled_job('cron', month='1-12', day_of_week='fri', hour='8')
def auto_run():
    # xx()
    print(time.strftime('%Y-%M-%D %H:%M:%S', time.localtime(time.time())))


# sched = BlockingScheduler()
# sched.add_job(auto_run, 'interval', seconds=5)
# sched.start()

if __name__ == '__main__':
    sched.start()