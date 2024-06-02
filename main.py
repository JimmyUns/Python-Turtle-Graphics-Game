import turtle
import time
import random
import config as cfg
import graphics
import player as p
import enemy as e
import enemy as bs
import bullet as b
import collision as c
import score as sc

wn = graphics.setup_screen()
graphics.draw_border()
graphics.register_shapes()

player = p.create_player()
enemies = e.create_enemies()
bullets = []
ebullets = []
score_pen = sc.create_score_pen()

score = 0
Game_Over = False
missed_enemies = 0
last_shot_time = 0
boss_summoned = False

esps = 2 #enemy shootings per second
eindex = 0 #enemy index
nst = 0.0 #next shooting time

turtle.listen() #update player
turtle.onkey(lambda: p.move_left(player), "Left")
turtle.onkey(lambda: p.move_right(player), "Right")
turtle.onkey(lambda: fire_bullet(), "Up")

sc.update_score(score_pen, score)

def fire_bullet():
    global last_shot_time
    current_time = time.time() * 1000
    if current_time - last_shot_time >= cfg.SHOOTING_COOLDOWN:
        last_shot_time = current_time
        b.fire_bullet(bullets, player)
while True:
    for enemy in enemies: #update enemies
        x = enemy.xcor()
        x += cfg.ENEMYSPEED
        enemy.setx(x)

        if(boss_summoned == False):
            if(time.time() * 1000 > nst):
                esps = 2
                eindex = 0
                nst = (time.time() * 1000) + 3000

            if(esps > 0): #enemy shooting
                eindex += 1
                if eindex <= esps:
                    b.fire_ebullet(ebullets, enemy)
                else:
                    rNum = random.randint(0, 1)
                    if rNum >= 0.5:
                        b.fire_ebullet(ebullets, enemy)
                esps -= 1

        if enemy.xcor() > 270 or enemy.xcor() < -270:
            cfg.ENEMYSPEED *= -1
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and not Game_Over:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()

        for bullet in bullets: #update bullets
            if(boss_summoned == False):
                if c.is_collision(bullet, enemy, 25):
                    bullet.hideturtle()
                    bullets.remove(bullet)
                    bullet.setposition(0, -400)
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    enemy.setposition(x, y)
                    cfg.ENEMYSPEED += 0.5
                    score += 10
                    sc.update_score(score_pen, score)
            else:
                if c.is_collision(bullet, enemy, 100):
                    bullet.hideturtle()
                    bullets.remove(bullet)
                    bullet.setposition(0, -400)
                    cfg.ENEMYSPEED += 2
                    score -= 10
                    sc.update_score(score_pen, score)


        if c.is_collision(player, enemy, 30):
            Game_Over = True

        if Game_Over:
            player.hideturtle()
            for bullet in bullets:
                bullet.hideturtle()
                bullet.clear()
            bullets = [None] * len(bullets)
            bullets.clear()
    
            for e in enemies:
                e.hideturtle()
                e.clear()
            enemies = [None] * len(enemies)
            enemies.clear()
            break

    if(boss_summoned == False):
        if(score >= 50):
            for e in enemies:
                e.hideturtle()
                e.clear()
            enemies = [None] * len(enemies)
            enemies.clear()
            enemies = bs.create_boss()
            boss_summoned = True
            for eb in ebullets:
                eb.hideturtle()
                eb.clear()
            ebullets = [None] * len(bullets)
            ebullets.clear()
    else:
        if(score <= 0):
            player.hideturtle()
            for bullet in bullets:
                bullet.hideturtle()
                bullet.clear()
            bullets = [None] * len(bullets)
            bullets.clear()
                
            for e in enemies:
                e.hideturtle()
                e.clear()
            enemies = [None] * len(enemies)
            enemies.clear()
            graphics.close_border()
            break

    b.move_bullets(bullets)
    b.move_ebullets(ebullets)
    wn.update()
