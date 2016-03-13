import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_line(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(180)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(40)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    #Create the turtle angie
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #Create turtle triangle
    nick = turtle.Turtle()
    nick.shape("turtle")
    nick.color("green")
    nick.speed(20)

    for i in range(1,36):
        draw_line(nick)
        nick.right(4)

    window.exitonclick()

draw_art()
