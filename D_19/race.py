from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=800, height=600)
bet = screen.textinput(title='Make a bet', prompt='Which color will win the race?').lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#timmy = Turtle(shape='turtle')
#timmy.penup()

def main():    
    set_start()
    screen.exitonclick()

def set_start():
    posx = -350
    posy = -150
    gap = 50
    for i in range(0, 6):
        turtle = Turtle(shape='turtle')
        turtle.penup()
        turtle.color(colors[i])
        turtle.goto(x=posx, y=posy+(i*gap))


if __name__ == '__main__':
    main()