from turtle import Screen, Turtle, getcanvas
from block import Block, BLOCK_WIDTH, BLOCK_HEIGHT
from ball import Ball
from player import Player, PLAYER_WIDTH
import time

BLOCKS_PER_ROW = 14
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
PADDING_TOP = 70
SPACING_BLOCKS = 15
FONT = ('Courier', 30, 'bold')
NUMBER_OF_ROWS = 6

def move_player(event):
    global game_started
    if not game_started:
        game_started = True
    player_x = event.x - (SCREEN_WIDTH / 2)
    left_edge = row_x_start + PLAYER_WIDTH / 2
    right_edge =  row_x_end - PLAYER_WIDTH / 2

    if player_x < left_edge:
        player_x  = left_edge

    elif player_x > right_edge:
        player_x = right_edge

    else:
        player.goto(player_x, -260)

def update_score(score):
    score_turtle.pu()
    score_turtle.clear()
    score_turtle.goto(0, SCREEN_HEIGHT / 2 - 50)
    score_turtle.write(score, font=FONT, align='center')

def game_over_screen(score):
    score_turtle.pu()
    score_turtle.clear()
    score_turtle.goto(0, -40)
    score_turtle.write(f"Score: {score}", font=FONT, align='center')
    score_turtle.color("red")
    score_turtle.goto(0, 0)
    score_turtle.write("Game Over", font=FONT, align='center')

def won_game(score):
    score_turtle.pu()
    score_turtle.clear()
    score_turtle.goto(0, -40)
    score_turtle.write(f"Perfect score!: {score}", font=FONT, align='center')
    score_turtle.color("green")
    score_turtle.goto(0, 0)
    score_turtle.write("Game  Won", font=FONT, align='center')
 
screen = Screen()

screen.bgcolor("black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.tracer(0)

turtle = Turtle(visible=False)
turtle.color("white")
turtle.pensize(5)

row_x_start = - (BLOCK_WIDTH + SPACING_BLOCKS) * (BLOCKS_PER_ROW / 2) + ((BLOCK_WIDTH + SPACING_BLOCKS) / 2) - (BLOCK_WIDTH + SPACING_BLOCKS) / 2
row_x_end = (BLOCK_WIDTH + SPACING_BLOCKS) * (BLOCKS_PER_ROW / 2) - ((BLOCK_WIDTH + SPACING_BLOCKS) / 2) + (BLOCK_WIDTH + SPACING_BLOCKS) / 2
turtle.pu()
turtle.goto(row_x_start, SCREEN_HEIGHT / 2)
turtle.pd()
turtle.goto(row_x_start, - SCREEN_HEIGHT / 2)
turtle.pu()
turtle.goto(row_x_end, SCREEN_HEIGHT / 2)
turtle.pd()
turtle.goto(row_x_end, - SCREEN_HEIGHT / 2)

blocks = []
for row in range(NUMBER_OF_ROWS):
    row_y_start = (SCREEN_HEIGHT / 2 ) - PADDING_TOP - BLOCK_HEIGHT / 2
    y = row_y_start - row * (BLOCK_HEIGHT + SPACING_BLOCKS)
    for col in range(BLOCKS_PER_ROW):
        x = row_x_start + (BLOCK_WIDTH + SPACING_BLOCKS) / 2 + col * (BLOCK_WIDTH + SPACING_BLOCKS)
        b = Block(x=x, y=y)

        blocks.append(b)

ball = Ball()

player = Player()
score_turtle = Turtle(visible=False)
score_turtle.color("white")
update_score(0)

canvas = getcanvas()
canvas.bind('<Motion>', move_player)

game_started = False
game_over = False
while not game_over:
    time.sleep(0.001)
    screen.update()
    if game_started:
        ball.move()
        ball.detect_collision_with_player(player.xcor(), player.ycor())
        ball.detect_collision_with_wall(row_x_start, row_x_end)
        if ball.detect_collision_with_block(blocks):
            player.score += 1
            update_score(player.score)
        if ball.detect_if_out_of_screen():
            game_over = True
            game_over_screen(player.score)
        if player.score >= BLOCKS_PER_ROW * NUMBER_OF_ROWS:
            game_over = True
            won_game(player.score)


screen.mainloop()
