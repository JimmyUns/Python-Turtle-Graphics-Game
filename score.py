import turtle

def create_score_pen():
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(0, 280)
    score_pen.hideturtle()
    return score_pen

def update_score(score_pen, score):
    score_pen.clear()
    scorestring = "Score: %s" % score
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
