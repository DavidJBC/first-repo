import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square with Python Turtle")

# Create a turtle object
drawer = turtle.Turtle()

# Pen Set up
drawer.width(5)
drawer.speed(5) 
drawer.left(180)
drawer.penup()
drawer.forward(650)
drawer.pendown()

# Letter K
drawer.right(90)
drawer.forward(200)
drawer.right(180)
drawer.forward(400)
drawer.right(180)
drawer.forward(200)

drawer.right(45)
drawer.forward(270)
drawer.right(180)
drawer.forward(270)
drawer.left(90)
drawer.forward(270)

# Letter U
drawer.penup()
drawer.left(45)
drawer.forward(50)
drawer.left(90)
drawer.forward(380)
drawer.pendown()

drawer.right(180)
drawer.forward(300)
drawer.circle(100, 180)
drawer.forward(300)

# Letter P
drawer.right(90)
drawer.penup()
drawer.forward(50)
drawer.pendown()

drawer.right(90)
drawer.forward(400)
drawer.backward(230)
drawer.left(40)
drawer.circle(110, 280)

# Letter A
drawer.penup()
drawer.right(140)
drawer.forward(35)
drawer.right(90)
drawer.forward(350)
drawer.pendown()
drawer.right(110)
drawer.forward(430)

drawer.backward(430)
drawer.left(45)
drawer.forward(430)

drawer.right(180)
drawer.forward(215)
drawer.left(65)
drawer.forward(160)
drawer.right(90)

# Letter L
drawer.penup()
drawer.forward(200)
drawer.right(90)
drawer.forward(340)
drawer.pendown()

drawer.right(90)
drawer.forward(400)
drawer.left(90)
drawer.forward(170)

screen.exitonclick()
