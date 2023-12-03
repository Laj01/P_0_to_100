from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.color('red')
    timmy.shape('turtle')

    sides = [3, 4, 5, 6, 7, 8, 9, 10,]

    for side in sides:
        i = 0
        while i < side:
            timmy.forward(100)
            timmy.right(360 / side)
            i += 1

    timmy.screen.mainloop()


if __name__ == '__main__':
    main()