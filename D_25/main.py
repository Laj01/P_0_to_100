import turtle
import pandas as pd

SCREEN_PATH = 'blank_states_img.gif'
DATA_PATH = '50_states.csv'

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title('US States')
image = SCREEN_PATH
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv(DATA_PATH, sep=',')

states = data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:
    popup_title = f'{len(guessed_states)}/50 States correct'
    answer = screen.textinput(title=popup_title, prompt='Guess the name of the states:').title()


    if answer in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data['state'] == answer]
        t.goto(int(state_data['x']), int(state_data['y']))    
        t.write(answer)
        guessed_states.append(answer)
        


turtle.mainloop()