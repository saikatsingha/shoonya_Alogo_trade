import time
import datetime

start_time = datetime.datetime(year=2023, month=4, day=9, hour=20, minute=40, second=00)
relativedelta = datetime.timedelta(hours=1)
iteration_time = datetime.timedelta(minutes=5)

end_time = start_time + relativedelta
last_run = None


def func():
    print("this is python")

market_end_time = datetime.datetime(year=2023, month=4, day=10, hour=15, minute=30, second=00)
while True:
    current_time = datetime.datetime.now()
    if current_time <= market_end_time:
        if last_run:
            if current_time >= last_run + iteration_time:
                func()
                last_run = current_time
        else:
            last_run = current_time
    elif current_time > end_time:
        break

    time.sleep(1)