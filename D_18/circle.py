from turtle import Turtle, Screen
import random
from color import random_color


def main():
    timmy = Turtle() 
    timmy.shape()
    timmy.speed('fastest')
    timmy.screen.colormode(255)

    for _ in range(36):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(-10)

    timmy.screen.mainloop()


if __name__ == '__main__':
    main()