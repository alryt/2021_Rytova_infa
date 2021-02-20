import turtle

turtle.shape('turtle')
turtle.speed(1)

n=100

def krug():
    turtle.circle(n)

turtle.begin_fill()
krug()
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(-40,30)
turtle.pendown()

def rot():
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)


turtle.begin_fill()
rot()
turtle.color('black')
turtle.end_fill()
turtle.penup()
turtle.goto(40,120)
turtle.pendown()
n=15

turtle.color('black')
turtle.begin_fill()
turtle.color('red')
krug()
turtle.end_fill()