number = eval(input("Enter an integer from 0 to 1000 : "))

num1 = number % 10
new_number1 = number // 10

num2 = new_number1 % 10
new_number2 = new_number1 // 10

num3 = new_number2 % 10
new_number3 = new_number2 // 10

num4 = new_number3 % 10
new_number4 = new_number3 // 10

print("The sum of the numbers you entered is", num1 + num2 + num3 + num4)
print(num4)
print(num3)
print(num2)
print(num1)
