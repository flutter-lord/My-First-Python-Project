minutes = eval(input("Enter the number of minutes you want to convert : "))

numberOfDays = minutes / (60 * 24)

numberOfYearsNow = int(numberOfDays // 365)

currentDays = int(numberOfDays % 365)

print(minutes,"minutes =", numberOfYearsNow, "years and", currentDays, "days")




