import turtle

t =turtle

circle_radius = eval(input("please, Enter the radius of the circle : "))


t.penup()
t.goto(-69, 00)
t.pendown()
t.circle(circle_radius)

t.penup()
t.goto(30, 0)
t.pendown()
t.circle(circle_radius)

t.penup()
t.goto(30, -99)
t.pendown()
t.circle(circle_radius)

t.penup()
t.goto(-69, -99)
t.pendown()
t.circle(circle_radius)

t.penup()
t.goto(-100, 100)
t.pendown()
t.forward(180)

t.right(90)
t.forward(200)

t.right(90)
t.forward(180)

t.right(90)
t.forward(200)

t.done()






