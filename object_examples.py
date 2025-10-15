''' n = 7777

print(id(n))

print(type(n))

my_name = "RicHARd"

print(my_name.strip())

money = 88776543

print(format(money, "o"))
print(format(money, ".7%"))

print(format(12345678.923, "9.1e"))

print(format(0.457467657, "9.3%"))
'''

import turtle as t
t.penup()
t.goto(50, 70)
t.pendown()
t.forward(100)
t.setheading(270)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.home()
t.pendown()

t.dot(500, "grey")

'''
t.forward(120)
t.setx(60)
t.sety(50)
t.right(90)
t.forward(100)
t.pencolor("red")
t.backward(100)
t.circle(50)
t.color("blue")
t.right(70)
t.circle(50)
'''

t.done()