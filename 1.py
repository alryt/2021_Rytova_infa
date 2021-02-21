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
turtle.goto(30,120)
turtle.pendown()
n=15

turtle.color('black')
turtle.begin_fill()
krug()
turtle.color('red')
turtle.end_fill()
turtle.penup()
turtle.goto(-60,120)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
n=25
krug()
turtle.color('red')
turtle.end_fill()

turtle.penup()
turtle.goto(37,120)
n=7

turtle.pendown()
turtle.begin_fill()
krug()
turtle.color('black')
turtle.end_fill()

turtle.penup()
turtle.goto(-50,120)
n=15
turtle.pendown()
turtle.begin_fill()
krug()
turtle.color('black')
turtle.end_fill()

turtle.penup()
turtle.goto(45,135)
turtle.pendown()

turtle.begin_fill()
turtle.left(100)
turtle.forward(30)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(30)
turtle.color('black')
turtle.end_fill()

turtle.penup()
turtle.goto(-35,145)
turtle.pendown()
turtle.begin_fill()
turtle.left(150)
turtle.forward(40)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(30)
turtle.color('black')
turtle.end_fill()








