import turtle
from config import *

def create_player():
    player = turtle.Turtle()
    player.shape(PLAYER_IMAGE)
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
    return player

def move_left(player):
    x = player.xcor()
    x -= PLAYERSPEED
    if x < -BORDER_SIZE + 20:
        x = -BORDER_SIZE + 20
    player.setx(x)

def move_right(player):
    x = player.xcor()
    x += PLAYERSPEED
    if x > BORDER_SIZE - 20:
        x = BORDER_SIZE - 20
    player.setx(x)
