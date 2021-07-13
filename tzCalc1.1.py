import datetime, pytz


#Import the datetime module and display the current date
currentTime = datetime.datetime.now()

#Import the datetime module for current day
currentDay = datetime.datetime.now().day

print ('\n\nFor timezone input you must type in timezone when prompted exactly as it is seen\n\n''US/Hawaii\n''America/Los_Angeles\n''America/Denver\n''America/Chicago\n''America/New_York\n'
    'Europe/London\n''Europe/Paris\n''Asia/Tokyo\n''Australia/Sydney\n\n')

#Defining user inputs
timezone = input("your timezone: ")
days = int(input("days away: "))
hours = int(input("Hour(24): "))
minutes = int(input("Minutes(60): "))

#Import Hawaii timezone as source timezone for base reference
sourceTimezone = pytz.timezone(timezone)

#Calculate user inputs ontop of current time for projected time in different timezones
timeCalc = currentTime.replace(day=(currentDay)+(days), hour=(hours),minute=(minutes), second=0, microsecond=0)

#Localize datetime to HST
userTimezone = sourceTimezone.localize(timeCalc)

#current time
print (
    f"\n{datetime.datetime.now()}"
    )

#hawaii
hawaii = pytz.timezone ('US/Hawaii')
nextHawaii = userTimezone.astimezone(hawaii)
print (
    f"\n{'Hawaii:':<15} {nextHawaii.strftime('%D %I:%M:%S %p'):>20}"
    )

#Pacific
pacific = pytz.timezone ('America/Los_Angeles')
nextPacific = userTimezone.astimezone(pacific)
print (
    f"\n{'Pacific:':<15} {nextPacific.strftime('%D %I:%M:%S %p'):>20}"
    )

#Mountain
mountain = pytz.timezone ('America/Denver')
nextMountain = userTimezone.astimezone(mountain)
print (
    f"\n{'Mountain:':<15} {nextMountain.strftime('%D %I:%M:%S %p'):>20}"
    )

#Central
central = pytz.timezone ('America/Chicago')
nextCentral = userTimezone.astimezone(central)
print (
    f"\n{'Central:':<15} {nextCentral.strftime('%D %I:%M:%S %p'):>20}"
    )

#Eastern
eastern = pytz.timezone ('America/New_York')
nextEastern = userTimezone.astimezone(eastern)
print (
    f"\n{'Eastern:':<15} {nextEastern.strftime('%D %I:%M:%S %p'):>20}"
    )

#London
london = pytz.timezone ('Europe/London')
nextLondon = userTimezone.astimezone(london)
print (
    f"\n{'London:':<15} {nextLondon.strftime('%D %I:%M:%S %p'):>20}"
    )

#Central Europe
centralEurope = pytz.timezone ('Europe/Paris')
nextCentralEurope = userTimezone.astimezone(centralEurope)
print (
    f"\n{'CentralEurope:':<15} {nextCentralEurope.strftime('%D %I:%M:%S %p'):>20}"
    )

#Japan/Korea
tokyo = pytz.timezone ('Asia/Tokyo')
nextTokyo = userTimezone.astimezone(tokyo)
print (
    f"\n{'Tokyo:':<15} {nextTokyo.strftime('%D %I:%M:%S %p'):>20}"
    )

#Australia/Sydney
sydney = pytz.timezone ('Australia/Sydney')
nextSydney = userTimezone.astimezone(sydney)
print (
    f"\n{'Sydney:':<15} {nextSydney.strftime('%D %I:%M:%S %p'):>20}\n"
    )

input('Press ENTER to exit')

