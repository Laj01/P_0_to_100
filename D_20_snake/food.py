from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)
    
