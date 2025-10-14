import turtle
x1, y1, x2, y2 = eval(input("Enter the coordinates of two lines, x1, y1, x2, y2 : "))

distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

t = turtle

t.penup()
t.goto(x1, y1)
t.pendown()
t.write("Point1")

t.goto(x2,y2)
t.write("Point2")

t.goto((x1 + x2) / 2 , (y1 + y2) / 2)

t.write(distance)
t.done()