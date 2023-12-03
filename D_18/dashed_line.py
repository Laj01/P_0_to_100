from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.color('red')
    timmy.shape('turtle')

    for _ in range(25):
        timmy.pd()
        timmy.forward(10)
        timmy.pu()
        timmy.forward(10)

    timmy.screen.mainloop()


if __name__ == '__main__':
    main()