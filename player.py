START_POS = (0, -230)
MOVE = 10
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('gold')
        self.shapesize(1, 1)
        self.goto(START_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE)

    def reset(self):
        self.goto(START_POS)