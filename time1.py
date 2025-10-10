import time
zonalTimeHours = eval(input("Enter the time zone according to GMT, add the sign, e.g +5, -3 : "))

currentTime = time.time()

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60
currentHours = totalHours % 24

yourHoursNow = currentHours + zonalTimeHours

print("The current time in your country now is", yourHoursNow, ":", currentMinutes,":", currentSeconds,"")






