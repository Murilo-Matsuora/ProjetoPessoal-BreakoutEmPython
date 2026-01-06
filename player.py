from turtle import Turtle
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 15

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="square", visible=True)
        self.pu()
        self.color("white")
        self.goto(0 , -260)
        self.shapesize(stretch_len=PLAYER_WIDTH/20, stretch_wid=PLAYER_HEIGHT/20)
        self.score = 0

        