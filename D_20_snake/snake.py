from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0),]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            part = Turtle(shape='square')
            part.color('white')
            part.penup()
            part.goto(position)
            self.parts.append(part)

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            newx = self.parts[part_num - 1].xcor()
            newy = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(newx, newy)
        self.parts[0].forward(MOVE_DISTANCE)