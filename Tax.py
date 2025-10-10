import time

'''purchaseAmount = eval(input("Enter purchase amount : "))

tax = purchaseAmount * 0.06

newTax = int(tax * 100) / 100

print(newTax)'''

currentTime = time.time()

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60
currentHours = totalHours % 24

print("The current time now is", currentHours,":", currentMinutes,":", currentSeconds,"GMT")

CURRENTNIGERIAHOUR = currentHours + 1

print("The current Nigerian time now is", CURRENTNIGERIAHOUR, ":", currentMinutes,":", currentSeconds,"WAT")






