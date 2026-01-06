from turtle import Turtle
BLOCK_WIDTH=60
BLOCK_HEIGHT=15

class Block(Turtle):
    def __init__(self, x, y):
        super().__init__(shape="square", visible=True)
        self.pu()
        self.color("white")
        self.goto(x , y)
        self.shapesize(stretch_len=BLOCK_WIDTH/20, stretch_wid=BLOCK_HEIGHT/20)
    
    def deactivate(self):
        self.hideturtle()