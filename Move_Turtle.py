import turtle

def go_up():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def go_right():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)

def go_down():
    turtle.setheading(270)
    turtle.stamp()
    turtle.forward(50)

def go_left():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def reset():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(go_up, 'w')
turtle.onkey(go_right, 'd')
turtle.onkey(go_down, 's')
turtle.onkey(go_left, 'a')
turtle.onkey(reset, 'Escape')

turtle.listen()

turtle.exitonclick()
