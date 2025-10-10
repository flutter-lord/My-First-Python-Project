import turtle

circleRadius = eval(input("please, Enter the radius of the circle : "))

t =turtle

t.penup()
t.goto(-69, 00)
t.pendown()
t.circle(circleRadius)

t.penup()
t.goto(30, 0)
t.pendown()
t.circle(circleRadius)

t.penup()
t.goto(30, -99)
t.pendown()
t.circle(circleRadius)

t.penup()
t.goto(-69, -99)
t.pendown()
t.circle(circleRadius)

t.done()






