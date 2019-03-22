import turtle
a=turtle.Turtle()
a.penup()
a.goto(0,-100)
a.pendown()
a.begin_fill()
a.fillcolor("yellow")
a.circle(100)
a.end_fill()

a.penup()
a.goto(-67,-40)
a.setheading(-60)
a.width(5)
a.pendown()
a.circle(-80 , -120)
a.fillcolor("black")
for i in range(-35,105,70):
    a.penup()
    a.goto(i, 35)
    a.setheading(0)
    a.pendown()
    a.begin_fill()

    a.circle(10)
    a.end_fill()

turtle.done()