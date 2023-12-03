from turtle import Turtle, Screen
import random


def main():
    walk(50)    


def walk(steps):
    timmy = Turtle() 
    timmy.shape()
    timmy.pensize(15)
    timmy.speed('fast')
    colors = ['red', 'green', 'blue', 'orange', 'black', 'yellow', 'cyan', 'purple', 'CornflowerBlue','MidnightBlue','GreenYellow','AliceBlue','Lime','SkyBlue','DarkOrange',]
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        timmy.color(random.choice(colors))
        timmy.setheading(random.choice(directions))
        timmy.forward(30)

    timmy.screen.mainloop()


if __name__ == '__main__':
    main()