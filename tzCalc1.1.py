import datetime, pytz


#Import the datetime module and display the current date
currentTime = datetime.datetime.now()

#Import the datetime module for current day
currentDay = datetime.datetime.now().day

#Defining user inputs
days = int(input("days away: "))
hours = int(input("Hour(24): "))
minutes = int(input("Minutes(60): "))

#Import Hawaii timezone as source timezone for base reference
sourceTimezone = pytz.timezone('US/Hawaii')

#Calculate user inputs ontop of current time for projected time in different timezones
timeCalc = currentTime.replace(day=(currentDay)+(days), hour=(hours),minute=(minutes), second=0, microsecond=0)

#Localize datetime to HST
hawaii = sourceTimezone.localize(timeCalc)

#Pacific
pacific = pytz.timezone ('America/Los_Angeles')
nextPacific = hawaii.astimezone(pacific)
print (f"{'Pacific:':<15} {nextPacific.strftime('%D %I:%M:%S %p'):>20}")

#Mountain
mountain = pytz.timezone ('America/Denver')
nextMountain = hawaii.astimezone(mountain)
print (f"\n{'Mountain:':<15} {nextMountain.strftime('%D %I:%M:%S %p'):>20}")

#Central
central = pytz.timezone ('America/Chicago')
nextCentral = hawaii.astimezone(central)
print (f"\n{'Central:':<15} {nextCentral.strftime('%D %I:%M:%S %p'):>20}")

#Eastern
eastern = pytz.timezone ('America/New_York')
nextEastern = hawaii.astimezone(eastern)
print (f"\n{'Eastern:':<15} {nextEastern.strftime('%D %I:%M:%S %p'):>20}")

#London
london = pytz.timezone ('Europe/London')
nextLondon = hawaii.astimezone(london)
print (f"\n{'London:':<15} {nextLondon.strftime('%D %I:%M:%S %p'):>20}")

#Central Europe
centralEurope = pytz.timezone ('Europe/Paris')
nextCentralEurope = hawaii.astimezone(centralEurope)
print (f"\n{'CentralEurope:':<15} {nextCentralEurope.strftime('%D %I:%M:%S %p'):>20}")

#Japan/Korea
tokyo = pytz.timezone ('Asia/Tokyo')
nextTokyo = hawaii.astimezone(tokyo)
print (f"\n{'Tokyo:':<15} {nextTokyo.strftime('%D %I:%M:%S %p'):>20}")

#Australia/Sydney
sydney = pytz.timezone ('Australia/Sydney')
nextSydney = hawaii.astimezone(sydney)
print (f"\n{'Sydney:':<15} {nextSydney.strftime('%D %I:%M:%S %p'):>20}")

input('Press ENTER to exit')
