import time
import datetime

start_time = datetime.datetime(year=2023, month=4, day=10, hour=20, minute=00, second=00)
relativedelta = datetime.timedelta(hours=1)
iteration_time = datetime.timedelta(minutes=1)

end_time = start_time + relativedelta
last_run = None

start="09:15:00"
end="23:30:00"
start_dt = datetime.datetime.strptime(start, '%H:%M:%S')
end_dt = datetime.datetime.strptime(end, '%H:%M:%S')
diff = (end_dt - start_dt) 
diff.seconds/60 

print(start)
print(end)

start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
time.sleep(5)
end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
print total_time

# while True:
#     current_time = time.localtime()
#     if current_time <= market_end_time:
#         print(f"Current Time is {current_time }")
#         print (time.strftime("%H:%M:%S"))
#     else:
#         break

#     time.sleep(1)