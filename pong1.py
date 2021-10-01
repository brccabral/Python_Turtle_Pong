# sudo apt-get install python3-tk
# turtle was already included
import turtle

# wn = Window
wn = turtle.Screen()
wn.title("Pong by @brccabral")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # do not refresh screen, speeds up the game

# Main game loop
while True:
    wn.update()
