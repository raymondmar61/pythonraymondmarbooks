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

#Convert UTC to local date
#twittercreatedate = "Wed Jul 15 19:06:17 +0000 2020"
twittercreatedate = "Wed Jul 15 00:06:17 +0000 2020"
twittercreatedatestrptime = datetime.datetime.strptime(twittercreatedate,"%a %b %d %H:%M:%S %z %Y")
print(twittercreatedatestrptime) #print 2020-07-15 00:06:17+00:00
convertutctolocal = twittercreatedatestrptime.replace(tzinfo=pytz.utc).astimezone(localtimezone)
print(convertutctolocal) #print 2020-07-14 17:06:17-07:00
monthdateyear = convertutctolocal.strftime("%m/%d/%Y")
print(monthdateyear) #print 07/14/2020