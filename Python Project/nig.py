import turtle

screen = turtle.Screen()
screen.title("Nig")
screen.setup(width=2000, height=1000)

drawer = turtle.Turtle()
drawer.shape("arrow")

drawer.color("black")

drawer.width(5)
drawer.speed(5) 
drawer.left(180)
drawer.penup()
drawer.forward(650)
drawer.pendown()
#------------------------------------------------------------------------   
drawer.right(90)
drawer.forward(200)
drawer.right(180)
drawer.forward(400)
drawer.right(180)
drawer.forward(400)

drawer.right(165)
drawer.forward(420)
drawer.right(195)
drawer.forward(400)

#---------------------------------------------------------------------------
drawer.right(90)
drawer.penup()
drawer.forward(100)
drawer.forward(20)

drawer.pendown()
drawer.right(90)
drawer.forward(400)
drawer.right(90)
drawer.forward(50)
drawer.backward(100)
drawer.forward(50)
drawer.right(90)
drawer.forward(400)
drawer.right(90)
drawer.forward(50)
drawer.backward(100)
#---------------------------------------------------------------------------

drawer.penup()
drawer.forward(300)
drawer.pendown()
drawer.right(180)
drawer.circle(170, 270)

#------------------------------------------------------------------------------
screen.exitonclick()