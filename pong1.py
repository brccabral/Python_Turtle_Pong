# sudo apt-get install python3-tk
# turtle was already included
import turtle

# wn = Window
wn = turtle.Screen()
wn.title("Pong by @brccabral")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # do not refresh screen, speeds up the game

# Paddle A
paddle_a = turtle.Turtle() # create turtle object
paddle_a.speed(0) # animation speed, set to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0) # start position
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle() # create turtle object
paddle_b.speed(0) # animation speed, set to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0) # start position
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle() # create turtle object
ball.speed(0) # animation speed, set to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) # start position
ball.dx = 0.07 # ball speed X
ball.dy = 0.07 # ball speed Y

# Control paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
