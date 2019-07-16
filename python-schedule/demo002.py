import schedule
import time


def job():
    print(f"======job start {time.time()}======")
    time.sleep(10)
    print(f"======jod done {time.time()}======")


for i in range(2):
    schedule.every(2).seconds.do(job)


while True:
    schedule.run_pending()
    print(f"======main start {time.time()}======")
    print(len(schedule.jobs))
    time.sleep(3)
    print(f"======main done {time.time()}======")
