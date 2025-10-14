annual_interest_rate, number_of_years, loan_amount, = eval(input("Dear Valued loanee, Please enter the interest rate,"
 "the number of years you will use to pay your loan and loan amount : "))

monthly_interest_rate = annual_interest_rate / 1200

monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))

total_payment = monthly_payment * number_of_years * 12

print("The monthly payment for your loan is", int(monthly_payment * 100) / 100)
print("The total payment is", int(total_payment * 100) / 100)




