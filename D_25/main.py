import turtle
import pandas as pd

SCREEN_PATH = 'blank_states_img.gif'
DATA_PATH = '50_states.csv'

screen = turtle.Screen()
screen.title('US States')
image = SCREEN_PATH
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(DATA_PATH, sep=',')


correct_answers = 0
popup_title = f'{correct_answers}/50 States correct'
answer = screen.textinput(title=popup_title, prompt='Guess the name of the states:')
titled_answer = answer.title()

states = data['state'].to_list()


if titled_answer in states:
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data['state'] == titled_answer]
    t.goto(int(state_data.x), int(state_data.y))    
    t.write(titled_answer)
    correct_answers += 1


turtle.mainloop()