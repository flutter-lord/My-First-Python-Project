import time
zonal_time_hours = eval(input("Enter the time zone according to GMT, add the sign, e.g +5, -3 : "))

current_time = time.time()

total_seconds = int(current_time)
current_seconds = total_seconds % 60

total_minutes = total_seconds // 60
current_minutes = total_minutes % 60

total_hours = total_minutes // 60
current_hours = total_hours % 24

your_hours_now = current_hours + zonal_time_hours

print("The current time in your country now is", your_hours_now, ":", current_minutes,":", current_seconds,"")






