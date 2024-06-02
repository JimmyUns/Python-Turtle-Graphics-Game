import turtle
from config import *

def create_bullet():
    bullet = turtle.Turtle()
    bullet.shape(BULLET_IMAGE)
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    return bullet

def create_ebullet():
    bullet = turtle.Turtle()
    bullet.shape(EBULLET_IMAGE)
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    return bullet

def fire_bullet(bullets, player):
    new_bullet = create_bullet()
    x = player.xcor()
    y = player.ycor() + 10
    new_bullet.setposition(x, y)
    new_bullet.showturtle()
    bullets.append(new_bullet)

def fire_ebullet(ebullets, enemy):
    new_ebullet = create_ebullet()
    x = enemy.xcor()
    y = enemy.ycor() + 10
    new_ebullet.setposition(x, y)
    new_ebullet.showturtle()
    ebullets.append(new_ebullet)


def move_bullets(bullets):
    for bullet in bullets[:]:
        y = bullet.ycor()
        y += BULLETSPEED
        bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bullets.remove(bullet)
    
def move_ebullets(ebullets):
    for bullet in ebullets[:]:
        y = bullet.ycor()
        y -= EBULLETSPEED
        bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            ebullets.remove(ebullets)
