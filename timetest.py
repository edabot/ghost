import schedule
import time
from datetime import datetime 

def job(t):
    print("I'm doing it at " + str(t))
    return

schedule.every().minute.do(job, datetime.now())

while True:
    schedule.run_pending()