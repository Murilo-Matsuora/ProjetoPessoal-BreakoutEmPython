from turtle import Turtle

class Barrier(Turtle):
    def __init__(self, x):
        super().__init__(visible=False)
        self.pu()
        self.color("white")
        self.goto(0 , x)
        