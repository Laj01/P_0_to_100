from turtle import Turtle, Screen
from color import random_color


def main():
    timmy = Turtle() 
    timmy.shape()
    timmy.speed('fastest')
    timmy.screen.colormode(255)
    draw_circle(10, timmy)
    timmy.screen.mainloop()


def draw_circle(gap, turtle):
    for _ in range(int(360 / gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.right(gap * -1)    


if __name__ == '__main__':
    main()