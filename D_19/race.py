from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=800, height=600)
is_on = False
bet = screen.textinput(title='Make a bet', prompt='Which color will win the race?').lower()
if bet: is_on = True
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
racers = []


def main():    
    set_start()
    start_race()
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
        racers.append(turtle)


def start_race():
        global is_on
        while is_on:
            for racer in racers:
                if racer.xcor() > 380:
                    is_on = False
                    winner_color = racer.pencolor()
                    if bet == winner_color:
                        print(f'YOU WON. The {winner_color} turtle won!')
                    else:
                        print(f'YOU LOST. The {winner_color} turtle won!')
                rand_distance = random.randint(0, 10)
                racer.forward(rand_distance)


if __name__ == '__main__':
    main()