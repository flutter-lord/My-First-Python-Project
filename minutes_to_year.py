minutes = eval(input("Enter the number of minutes you want to convert : "))

number_of_days = minutes / (60 * 24)

number_of_years_now = int(number_of_days // 365)

current_days = int(number_of_days % 365)

print(minutes,"minutes =", number_of_years_now, "years and", current_days, "days")




