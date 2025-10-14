number = eval(input("Enter an integer from 0 to 1000 : "))

num1 = number % 10
newNumber1 = number // 10

num2 = newNumber1 % 10
newNumber2 = newNumber1 // 10

num3 = newNumber2 % 10
newNumber3 = newNumber2 // 10

num4 = newNumber3 % 10
newNumber4 = newNumber3 // 10

print("The sum of the numbers you entered is", num1 + num2 + num3 + num4)
print(num4)
print(num3)
print(num2)
print(num1)
