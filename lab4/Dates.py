#ex1
import datetime
x = datetime.datetime.now()
a=int(x.strftime("%d"))
print(a-5)
#ex2
import datetime
today=datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#ex3
import datetime
currentDatetime = datetime.datetime.now()
currentDatetimeWithoutMicroseconds = currentDatetime.replace(microsecond=0)
print("Datetime without microseconds:", currentDatetimeWithoutMicroseconds)
#ex4
import datetime
currentDatetime = datetime.datetime.now()
DDatetime=datetime.datetime(2024, 2, 24)
deltatime=currentDatetime-DDatetime
print(deltatime.total_seconds())