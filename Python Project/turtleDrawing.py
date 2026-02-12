import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square with Python Turtle")

screen.screensize()
screen.setup(width = 1.0, height = 1.0)

drawer = turtle.Turtle()

drawer.width(5)
drawer.speed(5)
#----------------------------------------------------------------------
drawer.forward(500)
drawer.right(90)
drawer.forward(500)
drawer.right(90)
drawer.forward(1000)
drawer.right(90)
drawer.forward(1000)
drawer.right(90)
drawer.forward(1000)

#----------------------------------------------------------------------


screen.exitonclick()