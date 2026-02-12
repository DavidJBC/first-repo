import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Etch-A-Sketch with Hold-to-Move")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Set up the turtle
etch_turtle = turtle.Turtle()
etch_turtle.shape("turtle")
etch_turtle.speed(5)

# Variables to track key presses
move_forward = False
move_backward = False
turn_left = False
turn_right = False

# Functions to set key press state
def start_move_forward():
    global move_forward
    move_forward = True

def stop_move_forward():
    global move_forward
    move_forward = False

def start_move_backward():
    global move_backward
    move_backward = True

def stop_move_backward():
    global move_backward
    move_backward = False

def start_turn_left():
    global turn_left
    turn_left = True

def stop_turn_left():
    global turn_left
    turn_left = False

def start_turn_right():
    global turn_right
    turn_right = True

def stop_turn_right():
    global turn_right
    turn_right = False

# Function to clear the screen
def clear_screen():
    etch_turtle.clear()
    etch_turtle.penup()
    etch_turtle.home()
    etch_turtle.pendown()

def penup():
    etch_turtle.penup()

def pendown():
    etch_turtle.pendown()

# Function to continuously move the turtle based on key states
def move():
    if move_forward:
        etch_turtle.forward(40)
    if move_backward:
        etch_turtle.backward(40)
    if turn_left:
        etch_turtle.left(15)
    if turn_right:
        etch_turtle.right(15)
    screen.ontimer(move, 50)  # Repeat the function every 50 milliseconds

# Key bindings to start and stop movement
screen.listen()
screen.onkeypress(start_move_forward, "Up")
screen.onkeyrelease(stop_move_forward, "Up")
screen.onkeypress(start_move_backward, "Down")
screen.onkeyrelease(stop_move_backward, "Down")
screen.onkeypress(start_turn_left, "Left")
screen.onkeyrelease(stop_turn_left, "Left")
screen.onkeypress(start_turn_right, "Right")
screen.onkeyrelease(stop_turn_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(penup, "u")
screen.onkey(pendown, "d")

# Start the movement loop
move()

# Keep the window open
screen.mainloop()
