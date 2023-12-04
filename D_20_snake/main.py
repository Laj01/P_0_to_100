from turtle import Turtle, Screen
import time
from snake import Snake

# Set up the starting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake')

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()