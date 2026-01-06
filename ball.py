from turtle import Turtle
import random
BALL_SIZE = 20
MAX_SPEED_X = 20
MAX_SPEED_Y = 20
ACCELERATION = 1.01
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 15
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 15
SCREEN_HEIGHT = 720

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle", visible=True)
        self.pu()
        self.color("white")
        self.goto(0 , -200)
        self.speed_x = (random.random() + 1) * random.choice([-1, 1])
        self.speed_y =( random.random() * 0.2 + 1)
    
    def move(self):
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)
    
    def detect_collision_with_player(self, x, y):
        if (x - PLAYER_WIDTH / 2 < self.xcor() < x + PLAYER_WIDTH / 2) and (self.ycor() - BALL_SIZE/2 < y + PLAYER_HEIGHT / 2) and (self.ycor() - BALL_SIZE/2 > y):
            self.goto(self.xcor(), y + PLAYER_HEIGHT / 2 + BALL_SIZE/2)
            self.speed_y *= -1

            if self.speed_x < MAX_SPEED_X and self.speed_y < MAX_SPEED_Y:
                self.speed_x *= ACCELERATION
                self.speed_y *= ACCELERATION

    def detect_collision_with_wall(self, left_x, right_x):
        if (self.xcor() - BALL_SIZE/2 < left_x):
            self.goto(left_x + BALL_SIZE/2, self.ycor())
            self.speed_x *= -1
        if (right_x < self.xcor() + BALL_SIZE/2):
            self.goto(right_x - BALL_SIZE/2, self.ycor())
            self.speed_x *= -1
        
        if self.ycor() + BALL_SIZE/2 > SCREEN_HEIGHT / 2:
            self.goto(self.xcor(),  SCREEN_HEIGHT / 2 - BALL_SIZE/2)
            self.speed_y *= -1

    def detect_collision_with_block(self, blocks):
        for block in blocks:
            if (block.xcor() - BLOCK_WIDTH / 2 < self.xcor() < block.xcor() + BLOCK_WIDTH / 2) and (self.ycor() + BALL_SIZE / 2 > block.ycor() - BLOCK_HEIGHT/2):
                overlap_side = (BLOCK_WIDTH / 2) + (BALL_SIZE / 2) - abs(self.xcor() - block.xcor())
                overlap_bottom = (BLOCK_HEIGHT / 2) + (BALL_SIZE / 2) - abs(self.ycor() - block.ycor())

                if overlap_bottom < overlap_side:
                    self.speed_y *= -1
                else:
                    self.speed_x *= -1

                block.deactivate()
                blocks.remove(block)

                return True
        
        return False
    
    def detect_if_out_of_screen(self):
        if self.ycor() < - SCREEN_HEIGHT / 2:
            return True
        return False
    
                