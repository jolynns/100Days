Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> from datetime import date
>>> 
>>> date
<type 'datetime.date'>
>>> datetime.date
<method 'date' of 'datetime.datetime' objects>
>>> datetime.today()
datetime.datetime(2018, 5, 27, 17, 43, 28, 291000)
>>> today = datetime.today()
>>> type(today)
<type 'datetime.datetime'>
>>> todaydate = date.today()
>>> type(todaydate)
<type 'datetime.date'>
>>> todaydate
datetime.date(2018, 5, 27)
>>> 
>>> 
>>> todaydate.month
5
>>> todaydate.year
2018
>>> 
>>> 
>>> christmas = date(2018, 12, 25)
>>> christmas
datetime.date(2018, 12, 25)
>>> christmas - todaydate
datetime.timedelta(212)
>>> (christmas - todaydate).days
212
>>> 
>>> if christmas is not today:
	print("nope, you still have " + str((christmas - todaydate).days) + " days until Christmas!")
else:
	print("Presents!")

	
nope, you still have 212 days until Christmas!
>>> 
>>> 
>>> from datetime import timedelta
>>> 
>>> t = timedelta(days=4, hours=10)
>>> type(t)
<type 'datetime.timedelta'>
>>> t.days
4
>>> t.seconds
36000
>>> t.seconds / 3600
10
>>> eta = timedelta(hours=6)
>>> today
datetime.datetime(2018, 5, 27, 17, 44, 0, 249000)
>>> eta
datetime.timedelta(0, 21600)
>>> today + eta
datetime.datetime(2018, 5, 27, 23, 44, 0, 249000)
>>> str(today + eta)
'2018-05-27 23:44:00.249000'
>>>  t.seconds / 60 /60
 
  File "<pyshell#42>", line 2
    t.seconds / 60 /60
    ^
IndentationError: unexpected indent
>>> t.seconds / 60 /60
10
>>> 
