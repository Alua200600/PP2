#Task1
from datetime import timedelta,datetime
x = datetime.now()
new_date = x - timedelta(days=5)
print(new_date)

#Task2
d0 = datetime.now()-timedelta(days=1)
d1 = datetime.now()
d2 = datetime.now()+timedelta(days=1)
print(f"yesterday : {d0}")
print(f"today : {d1}")
print(f"tomorrow: {d2}")

#Task3
x = datetime.now()
x1 = x.replace(microsecond=0)
print(f"without microseconds : {x1}")

#Task4
diffrence = (d2-d0).total_seconds()
print(diffrence)