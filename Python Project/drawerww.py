import turtle

screen = turtle.Screen()
screen.title("Tite")
screen.bgcolor("#ebf21b")
screen.setup(width=2000, height=1000)

drawer = turtle.Turtle()
drawer.shape("turtle")

drawer.color("black")

drawer.penup()
drawer.left(90)
drawer.forward(280)
drawer.pendown()

drawer.right(90)
drawer.forward(83)
drawer.backward(166)
drawer.forward(166)
drawer.left(54.8)

drawer.circle(102, 250)

drawer.penup()
drawer.forward(100)
drawer.right(124.5)
drawer.forward(74)
drawer.pendown()
drawer.right(90.2)
drawer.forward(160)
drawer.backward(450)
drawer.right(90)
drawer.forward(200)
drawer.left(90)
drawer.forward(450)

screen.exitonclick()
