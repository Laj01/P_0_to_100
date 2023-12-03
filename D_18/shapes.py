from turtle import Turtle, Screen
import random


def main():
    timmy = Turtle() 
    timmy.shape('turtle')

    colors = ['red', 'green', 'blue', 'orange', 'black', 'yellow', 'cyan', 'purple']
    sides = [3, 4, 5, 6, 7, 8, 9, 10,]

    for side in sides:
        i = 0
        timmy.color(random.choice(colors))
        while i < side:
            timmy.forward(100)
            timmy.right(360 / side)
            i += 1

    timmy.screen.mainloop()


if __name__ == '__main__':
    main()