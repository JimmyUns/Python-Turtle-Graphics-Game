import turtle
import random
from config import *

def create_enemies():
    enemies = []
    for _ in range(ENEMY_COUNT):
        enemy = turtle.Turtle()
        enemy.shape(ENEMY_IMAGE)
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        enemies.append(enemy)
    return enemies

def create_boss():
    enemies = []
    for _ in range(1):
        enemy = turtle.Turtle()
        enemy.shape(BOSS_IMAGE)
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        enemies.append(enemy)
    return enemies
