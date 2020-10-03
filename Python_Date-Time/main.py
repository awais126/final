import time
import datetime
print (f"Time in seconds since the epoch: %s" %time.time())
#Time in seconds since the epoch: 1349271346.46

print (f"Current date and time: " , datetime.datetime.now())
#Current date and time: 2012-10-03 15:35:46.461491

print (f"Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
#Or like this: 12-10-03-15-35

print (f"Current year: ", datetime.date.today().strftime("%Y"))
#Current year: 2012

print (f"Month of year: ", datetime.date.today().strftime("%B"))
#Month of year: October

print (f"Week number of the year: ", datetime.date.today().strftime("%W"))
#Week number of the year: 40

print (f"Weekday of the week: ", datetime.date.today().strftime("%w"))
#Weekday of the week: 3

print (f"Day of year: ", datetime.date.today().strftime("%j"))
#Day of year: 277

print (f"Day of the month : ", datetime.date.today().strftime("%d"))
#Day of the month : 03

print (f"Day of week: ", datetime.date.today().strftime("%A"))
#Day of week: Wednesday