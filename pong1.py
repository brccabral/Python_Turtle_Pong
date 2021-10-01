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

# Paddle B

# Ball

# Main game loop
while True:
    wn.update()
