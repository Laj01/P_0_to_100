from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def refresh_text(self):
        self.score += 1
        self.clear()
        self.update_score()
        