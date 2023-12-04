from turtle import Turtle, Screen

# Set up the starting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor('black')
screen.title('Snake')

# Add the starting snake body to the screen
start_positions = [(0, 0), (-20, 0), (-40, 0),]
for position in start_positions:
    part = Turtle(shape='square')
    part.color('white')
    part.penup()
    part.goto(position)      








screen.exitonclick()