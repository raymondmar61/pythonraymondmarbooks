import datetime

#Dates for datetime
datetimeyear = 2024
datetimemonth = 10
datetimedaynumber = 31
datetimehour = 20
datetimeminute = 45
datetimesecond = 12
datetimevariablenumbers = datetime.datetime(datetimeyear, datetimemonth, datetimedaynumber, datetimehour, datetimeminute, datetimesecond)
print(datetimevariablenumbers) #print 2024-10-31 20:45:12
now = datetime.datetime.now()
print(type(now)) #print <class 'datetime.datetime'>
print(now) #print 2024-01-22 22:57:41.371284
print(now.year) #print 2024
print(now.month) #print 1
print(now.day) #print 22
nowattributesasstring = ("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
print(nowattributesasstring) #print 1/22/2024 22:57:41
#Convert date to string or convert datetime to string use strftime.  datetimetobeconvertedtostringvariable.strftime(date format).  Also, datetime.datetime.strftime(datetimetobeconvertedtostringvariable, date format).
todaysdate = datetime.datetime.now()
print(todaysdate) #print 2024-01-23 00:55:11.532506
print(todaysdate.strftime("%Y")) #print 2024
print(todaysdate.strftime("%y")) #print 24.  Year without century or two digit year.
print(todaysdate.strftime("%m")) #print 01.  Month as decimal number.
print(todaysdate.strftime("%B")) #print January
print(todaysdate.strftime("%b")) #print Jan
print(todaysdate.strftime("%d")) #print 23.  Day of the month.
print(todaysdate.strftime("%j")) #print 023.  Numbered day of the year.  Aug 22 is the 234th day of the 2022 year.
print(todaysdate.strftime("%w")) #print 2.  Numbered day of the week.  Sun is 0.  Sat is 6.
print(todaysdate.strftime("%A")) #print Tuesday
print(todaysdate.strftime("%a")) #print Tue
print(todaysdate.strftime("%H")) #print 00.  24-hour clock
print(todaysdate.strftime("%I")) #print 12.  12-hour clock.
print(todaysdate.strftime("%M")) #print 55.  Minute.
print(todaysdate.strftime("%S")) #print 11  Second.
print(todaysdate.strftime("%p")) #print AM.  AM or PM.
print(todaysdate.strftime("%%")) #print %.  A percentage.
print(todaysdate.strftime("%b %d, %Y")) #print Jan 23, 2024
print(todaysdate.strftime("Today is %B %y, %Y.")) #print Today is January 24, 2024.
formatnowdatenumbers = now.strftime("%m/%d/%Y")
print(formatnowdatenumbers) #print 01/22/2024
formatnowdatenumberstwodigityear = now.strftime("%D")
print(formatnowdatenumberstwodigityear) #print 01/22/24
print(type(formatnowdatenumbers)) #print <class 'str'>
formatnowabbreviationdates = now.strftime("%a %b %d, %Y")
print(formatnowabbreviationdates) #print Mon Jan 22, 2024
today = datetime.datetime.today()
print(type(today)) #print <class 'datetime.datetime'>
print(today) #print 2024-01-22 22:57:41.371346
formattodayhyphens = today.strftime("%Y-%m-%d")
print(formattodayhyphens) #print 2024-01-22
monthnumber = 8
daynumber = 21
yearnumber = 2024
numbervariablesdate = datetime.date(yearnumber, monthnumber, daynumber)
print(type(numbervariablesdate)) #print <class 'datetime.date'>
print(numbervariablesdate) #print 2024-08-21
formatnumbervariablesdate = numbervariablesdate.strftime("%A %B %d, %Y")
print(formatnumbervariablesdate) #print Wednesday August 21, 2024
print(type(formatnumbervariablesdate)) #print <class 'str'>
#Convert string to date use strptime(string to be converted, date format)
stringdatemmddyy = "08/21/24"
stringtodatetime = datetime.datetime.strptime(stringdatemmddyy, "%m/%d/%y")
print(stringtodatetime) #print 2024-08-21 00:00:00
print(type(stringtodatetime)) #print <class 'datetime.datetime'>
stringdatemmddyyyy = "08/21/2024"
stringtodatetime = datetime.datetime.strptime(stringdatemmddyyyy, "%m/%d/%Y")
print(stringtodatetime) #print 2024-08-21 00:00:00
formatdatetimebacktostring = stringtodatetime.strftime("%m/%d/%Y")
print(formatdatetimebacktostring) #print 08/21/2024
#Abbreviate datetime module as dt
from datetime import datetime as dt
nowabbreviateddt = dt.now()
print(nowabbreviateddt)
print("%s/%s/%s" % (nowabbreviateddt.month, nowabbreviateddt.day, nowabbreviateddt.year))
print("{}/{}/{}".format(nowabbreviateddt.month, nowabbreviateddt.day, nowabbreviateddt.year))

#Dates and times for datetime
stringdatetime = "Thu Jan 20 20:03:55  2022"
print(stringdatetime) #print Thu Jan 20 20:03:55  2022
convertstringdatetime = datetime.datetime.strptime(stringdatetime, "%a %b %d %H:%M:%S  %Y")
print(convertstringdatetime) #print 2022-01-20 20:03:55
formatdateabbreviate = convertstringdatetime.strftime("%a %b %d, %y %H:%M:%S")
print(formatdateabbreviate) #print Thu Jan 20, 22 20:03:1642651435.  RM:  If the string date is incorrect. Python datetime module corrects the date; Thu Jan 19, 2022 is incorrect.  Wed Jan 19, 2022 Python corrected.
stringdatemmddyyyymilitarytime = "2024-08-21 14:36:27"
print(datetime.datetime.strptime(stringdatemmddyyyymilitarytime, "%Y-%m-%d %H:%M:%S")) #print 2020-08-21 14:36:27
convertmilitarytimestep1 = datetime.datetime.strptime(stringdatemmddyyyymilitarytime, "%Y-%m-%d %H:%M:%S")
print(convertmilitarytimestep1) #print 2024-08-21 14:36:27
print(type(convertmilitarytimestep1)) #print <class 'datetime.datetime'>
convertmilitarytimestep2 = datetime.datetime.strftime(convertmilitarytimestep1, "%m/%d/%y %I:%M:%S %p")
print(convertmilitarytimestep2) #print 08/21/24 02:36:27 PM
print(type(convertmilitarytimestep2)) #print <class 'str'>

#Use f strings for date and for time
from datetime import datetime
asofnow = datetime.now()
print(asofnow) #print 2025-12-22 14:14:03.316495
print(f"F strings for dates F strings for time {asofnow:%x}") #print F strings for dates F strings for time 12/22/25
print(f"F strings for dates F strings for time {asofnow:%c}") #print F strings for dates F strings for time Mon Dec 22 14:14:03 2025
print(f"F strings for dates F strings for time {asofnow:%H:%M:%S}") #print F strings for dates F strings for time 14:14:03

#Date calculations date
yearmonthday1 = datetime.date(2017, 1, 30)
print(yearmonthday1) #print 2017-01-30
formatdatefullspelling = yearmonthday1.strftime("%A %B %d, %Y")
print(formatdatefullspelling) #print Monday January 30, 2017
yearmonthday2 = datetime.date(2017, 2, 20)
print(yearmonthday2) #print 2017-02-20
datesdifference = yearmonthday2 - yearmonthday1
print(datesdifference) #print 21 days, 0:00:00
print(datesdifference.days) #print 21
formatdateabbreviate = todaysdatetime.strftime("%a %b %d, %y")
print(formatdateabbreviate) #print Fri Jan 19, 24
#You don't want to average times on hours, minutes, and seconds.  Convert all times into seconds, calculate the average, and convert back to hours, minutes, and seconds.
def averagetime(timelist):
    timelistinseconds = []
    for eachtimelist in timelist:
        print(eachtimelist) #print 1:23:54
        print(eachtimelist.split(":")) #print ['1', '23', '54']
        hour, minute, second = map(int, eachtimelist.split(":"))
        print(hour) #print 1
        print(minute) #print 23
        print(second) #print 54
        print((hour * 3600) + (minute * 60) + (second)) #print 5034
        eachtimelistinseconds = (hour * 3600) + (minute * 60) + (second)
        timelistinseconds.append(eachtimelistinseconds)
    print(timelistinseconds) #print [3540, 3660, 5034]
    print(sum(timelistinseconds) / len(timelistinseconds)) #print 4078.0
    averagetime = sum(timelistinseconds) / len(timelistinseconds)
    hours = divmod(averagetime, 3600)
    print(hours) #print (1.0, 478.0)
    minutes = divmod(hours[1], 60)
    print(minutes) #print (7.0, 58.0)
    seconds = divmod(minutes[1], 1)
    print(seconds) #print (58.0, 0.0)
    return ("Average time is {} hours, {} minutes, and {} seconds.".format(int(hours[0]), int(minutes[0]), int(seconds[0])))


print(averagetime(["00:59:00", "1:1:00", "1:23:54"])) #print Average time is 1 hours, 7 minutes, and 58 seconds.
#The datetime.timedelta() function takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds. There is no month or year keyword argument because "a month" or "a year" is a variable amount of time depending on the particular month or year. A timedelta object has the total duration represented in days, seconds, and microseconds. These numbers are stored in the days, seconds, and microseconds attributes, respectively. The total_seconds() method will return the duration in number of seconds alone. Passing a timedelta object to str() will return a nicely formatted, human-readable string representation of the object.
giventimereturntimeduration = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8) #RM:  delta is the better variable.  I used giventimereturntimeduration to quickly explain timedelta.
print("Number of days", giventimereturntimeduration.days) #print Number of days 11
print("Number of seconds from hours, minutes and seconds", giventimereturntimeduration.seconds)  #Number of seconds from hours, minutes and seconds 36548.  10 hours, 9 minutes, are 8 seconds total 36548 seconds.
print("Number of microseconds", giventimereturntimeduration.microseconds)  #Number of microseconds 0
print("Total number of seconds days, hours, minutes, seconds", giventimereturntimeduration.total_seconds()) #print Total number of seconds days, hours, minutes, seconds 986948.0.  RM: 986,948 is the number of seconds for 11 days, 10 hours, 9 minutes, and 8 seconds.
print("Return giventimereturntimeduration as a string " + str(giventimereturntimeduration)) #print Return giventimereturntimeduration as a string 11 days, 10:09:08
todaysdate = datetime.datetime.now()
print(todaysdate) #print 2024-01-23 00:55:11.532506
addonehundreddays = datetime.timedelta(days=100)
onehundreddayslaterdate = todaysdate + addonehundreddays
print(onehundreddayslaterdate) #print 2024-05-02 00:55:11.532506.  One hundred days later is May 2, 2024.
print(type(onehundreddayslaterdate)) #print <class 'datetime.datetime'>
print(onehundreddayslaterdate.strftime("%a %b %d, %Y")) #print Thu May 02, 2024

#Times for datetime
now = datetime.datetime.now()
print(now) #print 2024-01-22 23:23:14.365800
extracttimefromnow = datetime.datetime.strftime(now, "%I:%M:%S %p")
print(extracttimefromnow) #print 11:23:14 PM
print(type(extracttimefromnow)) #print <class 'str'>
import time
numberofsecondssinceJan011970 = time.time()
print(numberofsecondssinceJan011970) #print 1705999527.1418614
starttimer = time.time()
secondsforsleep = 5
time.sleep(secondsforsleep)
endtimer = time.time()
print("The timer is {} seconds.  The result is {}".format(secondsforsleep, endtimer - starttimer)) #print The timer is 5 seconds.  The result is 5.017960071563721
numberofsecondssinceepochtimestamp = 28800 #epoch timestamp is Jan 1, 1970 at 12:00am which is numberofsecondssinceepochtimestamp = 28800
print(datetime.datetime.fromtimestamp(numberofsecondssinceepochtimestamp)) #print 1970-01-01 00:00:00.  Jan 1, 1970 at 12:00:00am is the date and time 28800 seconds passed since Dec 31, 1969 at 4:00:00pm

#UTC
utcnow = datetime.datetime.utcnow()
print(utcnow)
import dateutil.tz
utclocalnow = datetime.datetime.now(dateutil.tz.tzlocal())
print(utclocalnow)
utclocalnowtimezone = datetime.datetime.now(dateutil.tz.tzlocal()).tzname()
print(utclocalnowtimezone)
#Convert UTC date and time
import pytz
utcdatestring = "Wed Jul 15 00:06:17 +0000 2024"
convertutcdatestringtodatetime = datetime.datetime.strptime(utcdatestring, "%a %b %d %H:%M:%S %z %Y")
print(convertutcdatestringtodatetime) #print 2024-07-15 00:06:17+00:00
print(type(convertutcdatestringtodatetime)) #print <class 'datetime.datetime'>
#https://stackoverflow.com/questions/2720319/python-figure-out-local-timezone
localtimezone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
print(localtimezone) #print PST.  RM:  We're not in daylight savings time PDT on Jan 22, 2024.
convertutctolocaltimezone = convertutcdatestringtodatetime.replace(tzinfo=pytz.utc).astimezone(localtimezone)
print(convertutctolocaltimezone) #print 2024-07-14 16:06:17-08:00
print(type(convertutctolocaltimezone)) #print <class 'datetime.datetime'>
extractmmddyyfromutc = datetime.datetime.strftime(convertutctolocaltimezone, "%m/%d/%Y")
print(extractmmddyyfromutc) #print 07/14/2024
print("\n")
#Another way convert UTC date and time
#Autodetect zone
fromzoneauto = dateutil.tz.tzutc()
print(fromzoneauto) #print tzutc()
tozoneauto = dateutil.tz.tzlocal()
print(tozoneauto) #print tzlocal()
#Hardcode UTC time zone
fromzone = dateutil.tz.gettz("UTC")
print(fromzone) #print tzfile('/usr/share/zoneinfo/UTC')
tozone = dateutil.tz.gettz('America/Los_Angeles')
print(tozone) #print tzfile('/usr/share/zoneinfo/America/Los_Angeles')
utcnow = datetime.datetime.utcnow()
print(utcnow) #print 2024-01-23 07:59:54.727125
utcnowstring = str(utcnow)
convertutcnow = datetime.datetime.strptime(utcnowstring, "%Y-%m-%d %H:%M:%S.%f")
print(convertutcnow) #print 2024-01-23 07:59:54.727125
print(type(convertutcnow)) #print <class 'datetime.datetime'>
convertutcnowformat = convertutcnow.replace(tzinfo=fromzone).astimezone(tozone)
print(convertutcnowformat) #print 2024-01-22 23:59:54.727125-08:00
print(type(convertutcnowformat)) #print <class 'datetime.datetime'>
changeutctimezone = dateutil.tz.gettz("America/New York")
print(changeutctimezone) #print tzfile('/usr/share/zoneinfo/America/New_York')
changeutcnowformatnewtimezone = convertutcnow.astimezone(changeutctimezone)
print(changeutcnowformatnewtimezone) #print 2024-01-23 10:59:54.727125-05:00
