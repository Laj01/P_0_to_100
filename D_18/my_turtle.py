from turtle import Turtle, Screen


def main():
    my_turtle = Turtle()
    my_turtle.shape('turtle')
    my_turtle.color('red')
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)

    my_turtle.screen.mainloop()
    



if __name__ == '__main__':
    main()