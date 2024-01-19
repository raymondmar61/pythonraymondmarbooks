import datetime

yearmonthday1 = datetime.date(2017, 1, 30)
print(yearmonthday1) #print 2017-01-30
formatdatefullspelling = yearmonthday1.strftime("%A %B %d, %Y")
print(formatdatefullspelling) #print Monday January 30, 2017
yearmonthday2 = datetime.date(2017, 2, 20)
print(yearmonthday2) #print 2017-02-20
datesdifference = yearmonthday2 - yearmonthday1
print(datesdifference) #print 21 days, 0:00:00
print(datesdifference.days) #print 21
todaysdatetime = datetime.datetime.now()
print(todaysdatetime) #print 2024-01-19 01:01:15.160350
formatdateabbreviate = todaysdatetime.strftime("%a %b %d, %y")
print(formatdateabbreviate) #print Fri Jan 19, 24
stringdatetime = "Thu Jan 20 20:03:55  2022"
print(stringdatetime) #print Thu Jan 20 20:03:55  2022
convertstringdatetime = datetime.datetime.strptime(stringdatetime, "%a %b %d %H:%M:%S  %Y")
print(convertstringdatetime) #print 2022-01-20 20:03:55
formatdateabbreviate = convertstringdatetime.strftime("%a %b %d, %y %H:%M:%S")
print(formatdateabbreviate) #print Thu Jan 20, 22 20:03:1642651435.  RM:  If the string date is incorrect. Python datetime module corrects the date; Thu Jan 19, 2022 is incorrect.  Wed Jan 19, 2022 Python corrected.
