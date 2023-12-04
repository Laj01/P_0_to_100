from turtle import Turtle


START_POSITIONS = [(0, 0), (-20, 0), (-40, 0),]
MOVE_DISTANCE = 20
UP = 90 
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        part = Turtle(shape='square')
        part.color('white')
        part.penup()
        part.goto(position)
        self.parts.append(part)

    def extend_snake(self):        
        self.add_part(self.parts[-1].position())

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            newx = self.parts[part_num - 1].xcor()
            newy = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    