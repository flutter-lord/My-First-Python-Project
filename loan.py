annualInterestRate, numberOfYears, loanAmount, = eval(input("Dear Valued loanee, Please enter the interest rate,"
 "the number of years you want to pay your loan and loan amount : "))

monthlyInterestRate = annualInterestRate / 1200

monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

print("The monthly payment for your loan is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) / 100)




