import datetime
import pytz

firstdate = datetime.date(2017, 1, 30)
print(firstdate) #print 2017-01-30
print(firstdate.strftime("%A %B %d, %Y")) #print Monday January 30, 2017
strftimevariable = firstdate.strftime("%A %B %d, %Y")
print(strftimevariable) #print Monday January 30, 2017
secondate = datetime.date(2017,2,1)
print(secondate) #print 2017-02-01
print(secondate - firstdate) #print 2 days, 0:00:00
print((secondate - firstdate).days) #print 2
print(datetime.datetime.now()) #print 2020-07-29 23:07:46.661061
print(datetime.datetime.now().strftime("%a %b %d, %Y")) #print Wed Jul 29, 2020
twittercreatedate = "Wed Jul 15 19:06:17 +0000 2020"
#twittercreatedate = "Wed Jul 15 19:06:17 2020"
convertstringtodatetime = datetime.datetime.strptime(twittercreatedate,"%a %b %d %H:%M:%S %z %Y")
print(twittercreatedate) #print Wed Jul 15 19:06:17 +0000 2020
print(convertstringtodatetime) #print 2020-07-15 19:06:17+00:00
mystringtodatetime = convertstringtodatetime.strftime("%A %B %d, %Y")
print(mystringtodatetime) #print Wednesday July 15, 2020

now = datetime.datetime.now()
print(now) #print 2020-08-21 14:51:46.004478
print(now.year) #print 2020
print(now.month) #print 8
print(now.day) #print 21
print(type(now)) #print <class 'datetime.datetime'>
print(now.strftime("%m/%d/%Y")) #print 08/21/2020
print("%s/%s/%s" % (now.month, now.day, now.year)) #print 8/21/2020
print(now.strftime("%m-%d-%y")) #print 08-21-20
print(now.strftime("%D")) #print 08/21/20
print("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)) #print 8/21/2020 14:51:46
nowdatetostring = now.strftime("%a %b %d, %Y")
print(nowdatetostring) #print Fri Aug 21, 2020
print(type(nowdatetostring)) #print <class 'str'>
nowtoday = datetime.datetime.today()
print(nowtoday) #print 2020-08-21 14:51:46.004533
print(type(nowtoday)) #print <class 'datetime.datetime'>
print(nowtoday.strftime("%Y-%m-%d")) #print 2020-08-21
month = 8
day = 21
year = 2020
variablesdate = datetime.date(year, month, day)
print(variablesdate) #print 2020-08-21
#variablesdateerror = datetime.date(month, day, year)
#print(variablesdateerror) #print ValueError: month must be in 1..12 #print 
variablesdatetostring = variablesdate.strftime("%A %B %d, %Y")
print(variablesdatetostring) #print Friday August 21, 2020
print(type(variablesdatetostring)) #print <class 'str'>
variablesdatetostringd = variablesdate.strftime("%D")
print(variablesdatetostringd) #print 08/21/20
print(type(variablesdatetostringd)) #print <class 'str'>

a = datetime.date(2011,11,24)
b = datetime.date(2011,11,17)
print(a-b) #print 7 days, 0:00:00
print((a-b).days) #print 7

#datetime.strptime() is used for converting a string to a datetime object , when using strptime() you have to specify the correct format in which the date/time in the string exists.
stringdatemmddyy = "08/21/20"
print(datetime.datetime.strptime(stringdatemmddyy,"%m/%d/%y")) #print 2020-08-21 00:00:00
print(type(datetime.datetime.strptime(stringdatemmddyy,"%m/%d/%y"))) #print <class 'datetime.datetime'>
stringdatemmddyyyy = "08-21-2020"
stringdatemmddyyyyvariable = datetime.datetime.strptime(stringdatemmddyyyy, "%m-%d-%Y")
print(stringdatemmddyyyyvariable) #print 2020-08-21 00:00:00
print(type(stringdatemmddyyyyvariable)) #print <class 'datetime.datetime'>
print(stringdatemmddyyyyvariable.strftime("%D")) #print 08/21/20
stringdatemmddyyyymilitarytime = "2020-08-21 14:36:27"
print(datetime.datetime.strptime(stringdatemmddyyyymilitarytime,"%Y-%m-%d %H:%M:%S")) #print 2020-08-21 14:36:27
converttoreadablefirststep = datetime.datetime.strptime(stringdatemmddyyyymilitarytime,"%Y-%m-%d %H:%M:%S")
converttoreadablesecondstep = datetime.datetime.strftime(converttoreadablefirststep, "%m/%d/%y %I:%M:%S %p")
print(converttoreadablesecondstep) #print 08/21/20 02:36:27 PM
print(type(converttoreadablesecondstep)) #print <class 'str'>
twitterstringdate = datetime.datetime.strftime(converttoreadablefirststep, "%m/%d/%y")
twitterstringtime = datetime.datetime.strftime(converttoreadablefirststep, "%I:%M:%S %p")
print(twitterstringdate) #print 08/21/20
print(type(twitterstringdate)) #print <class 'str'>
print(twitterstringtime) #print 02:36:27 PM
print(type(twitterstringtime)) #print <class 'str'>
#Use strftime to extract time and convert the 24 hour time from now() to 12 hour time
nowtime = datetime.datetime.now()
print(nowtime) #print 2020-08-21 14:51:46.010397
print(type(nowtime)) #print <class 'datetime.datetime'>
print(datetime.datetime.strftime(nowtime, "%I:%M:%S %p")) #print 02:51:46 PM
print(type(nowtime)) #print <class 'datetime.datetime'>
nowtime = datetime.datetime.strftime(nowtime, "%I:%M:%S %P")
print(nowtime) #print 02:51:46 pm
print(type(nowtime)) #print <class 'str'>

#UTC
#Convert UTC to local date
#twittercreatedate = "Wed Jul 15 19:06:17 +0000 2020"
twittercreatedate = "Wed Jul 15 00:06:17 +0000 2020"
twittercreatedatestrptime = datetime.datetime.strptime(twittercreatedate,"%a %b %d %H:%M:%S %z %Y")
print(twittercreatedatestrptime) #print 2020-07-15 00:06:17+00:00
convertutctolocal = twittercreatedatestrptime.replace(tzinfo=pytz.utc).astimezone(localtimezone)
print(convertutctolocal) #print 2020-07-14 17:06:17-07:00
monthdateyear = convertutctolocal.strftime("%m/%d/%Y")
print(monthdateyear) #print 07/14/2020
currentlocaltime = datetime.datetime.now()
print(currentlocaltime) #print 2020-07-29 23:07:46.663668
currentutctime = datetime.datetime.utcnow()
print(currentutctime) #print 2020-07-30 06:07:46.663672
#https://stackoverflow.com/questions/2720319/python-figure-out-local-timezone
localtimezone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
print(localtimezone) #print PDT
convertutctolocal = currentutctime.replace(tzinfo=pytz.utc).astimezone(localtimezone)
print(convertutctolocal) #print 2020-07-29 23:07:46.663672-07:00
import dateutil.tz
print(datetime.datetime.now(dateutil.tz.tzlocal())) #print 2020-07-29 23:07:46.666863-07:00
print(datetime.datetime.now(dateutil.tz.tzlocal()).tzname()) #print PDT
#https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local-datetime
from datetime import datetime
from dateutil import tz
#Hardcode Zone
fromzone = tz.gettz("UTC")
print(fromzone) #print tzfile('/usr/share/zoneinfo/UTC')
tozone = tz.gettz('America/Los_Angeles')
print(tozone) #print tzfile('/usr/share/zoneinfo/UTC')
tozone = tz.gettz('America/Los Angeles')
print(tozone) #print tzfile('/usr/share/zoneinfo/UTC')
#Autodetect zone
fromzoneauto = tz.tzutc()
print(fromzoneauto) #print tzutc()
tozoneauto = tz.tzlocal()
print(tozoneauto) #print tzlocal()
#Convert UTC time to present time zone or assigned a time zone
utcdatetimenow = datetime.utcnow()
print(utcdatetimenow) #print 2020-08-05 03:26:35.787015
strptimeutcdatetimenow = datetime.strptime(str(utcdatetimenow), "%Y-%m-%d %H:%M:%S.%f")
print(strptimeutcdatetimenow) #print 2020-08-05 03:26:35.787015
utcfromzone = strptimeutcdatetimenow.replace(tzinfo=fromzone)
print(utcfromzone) #print 2020-08-05 03:26:35.787015+00:00
utctozone = strptimeutcdatetimenow.astimezone(tozone)
print(utctozone) #print 2020-08-05 03:26:35.787015-07:00
tozone = tz.gettz('America/New York')
print(tozone) #print tzfile('/usr/share/zoneinfo/America/New_York')
utctozone = strptimeutcdatetimenow.astimezone(tozone)
print(utctozone) #print 2020-08-05 06:26:35.787015-04:00

