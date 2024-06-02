import turtle
import config as cfg

def setup_screen():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")
    return wn

def draw_border():
    border_pen = turtle.Turtle()
    border_pen.speed(6)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-cfg.BORDER_SIZE, -cfg.BORDER_SIZE)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(cfg.BORDER_SIZE * 2)
        border_pen.lt(90)
    border_pen.hideturtle()
    wn = turtle.Screen()
    wn.bgpic(cfg.BACKGROUND_IMAGE)

def close_border():
    border_pen = turtle.Turtle()
    border_pen.speed(2)
    border_pen.color("black")
    border_pen.penup()
    border_pen.setposition(-cfg.BORDER_SIZE, -cfg.BORDER_SIZE)
    border_pen.width(800)
    border_pen.pendown()
    for side in range(4):
        border_pen.fd(cfg.BORDER_SIZE * 2)
        border_pen.lt(90)
    border_pen.hideturtle()

def register_shapes():
    turtle.register_shape(cfg.ENEMY_IMAGE)
    turtle.register_shape(cfg.PLAYER_IMAGE)
    turtle.register_shape(cfg.BOSS_IMAGE)
    turtle.register_shape(cfg.BULLET_IMAGE)
    turtle.register_shape(cfg.EBULLET_IMAGE)
