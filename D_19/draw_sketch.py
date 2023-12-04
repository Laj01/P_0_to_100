from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def main():
    screen.onkey(clear_canvas, 'c')
    screen.onkey(move_forward, 'Up')
    screen.onkey(move_backward, 'Down')
    screen.onkey(turn_left, 'Left')
    screen.onkey(turn_right, 'Right')
    screen.listen()
    screen.exitonclick()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.back(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


def clear_canvas():
    timmy.reset()


if __name__ == '__main__':
    main()