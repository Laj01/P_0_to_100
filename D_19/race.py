from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600)

bet = screen.textinput(title='Make a bet', prompt='Which color will win the race?').lower()
def main():
    print(bet)


if __name__ == '__main__':
    main()