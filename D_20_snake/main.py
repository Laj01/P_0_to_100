from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Set up the starting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #collision detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh_text()

    #collision detection with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

    #collision detection with body
    for part in snake.parts:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()