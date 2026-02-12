import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square with Python Turtle")

# Create a turtle object
drawer = turtle.Turtle()
bawer = turtle.Turtle()

# Set the speed of the turtle
drawer.speed(10)
bawer.speed(10)
drawer.color("green")
bawer.color("green")

drawer.penup()
drawer.goto(-500,0)
drawer.pendown()
drawer.forward(1000)

bawer.penup()
bawer.goto(0,500)
bawer.pendown()
bawer.right(90)
bawer.forward(1000)

drawer.penup()
drawer.goto(0,500)
drawer.pendown()

drawer.right(45)
bawer.right(135)
bawer.forward(707.106781187)
drawer.forward(707.106781187)


drawer.right(90)
bawer.right(90)
bawer.forward(707.106781187)
drawer.forward(707.106781187)

drawer.right(45)
bawer.right(45)
bawer.forward(500)
drawer.forward(500)

for _ in range(2):
    drawer.right(90)
    bawer.right(90)
    bawer.forward(1000)
    drawer.forward(1000)


drawer.right(135)
bawer.right(135)
bawer.forward(1414.21356237)
drawer.forward(1414.21356237)

drawer.right(135)
bawer.right(135)
bawer.forward(1000)
drawer.forward(1000)

drawer.right(135)
bawer.right(135)
bawer.forward(1414.21356237)
drawer.forward(1414.21356237)

drawer.right(135)
bawer.right(135)
bawer.forward(250)
drawer.forward(250)

drawer.right(90)
bawer.right(90)
bawer.forward(1000)
drawer.forward(1000)

for _ in range(2):
    drawer.right(90)
    bawer.right(90)
    bawer.forward(250)
    drawer.forward(250)

drawer.right(90)
bawer.right(90)
bawer.forward(1000)
drawer.forward(1000)


# Close the window on click
screen.exitonclick()
