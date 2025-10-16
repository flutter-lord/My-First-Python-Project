four_digits = eval(input("Enter any four digits from 1000 to 9999 : "))

digit1 = four_digits // 1000
digit2 = (four_digits // 100) % 10
digit3 = (four_digits // 10) % 10
digit4 = four_digits % 10



print("The reverse of", four_digits, "is",str(digit4) + str(digit3) + str(digit2) +str(digit1))
