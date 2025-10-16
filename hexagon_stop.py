import turtle as t

t.hideturtle()
t.begin_fill()
t.fillcolor("red")
t.circle(100,steps= 6)
t.end_fill()

t.penup()
t.goto(-70, 70)
t.pendown()
t.color("white")
t.write("STOP", font= ("Arial", 40, "bold"))


t.done()
