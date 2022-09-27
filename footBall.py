## File Name:   footBall.py
## By:          Daniel Lucio  
## Version:     0.1
## Date:        2022-09-10
## Description: simple pong game program 

import turtle


## U.I 
wn = turtle.Screen()
wn.title("Football on the pitch by Danny")
wn.bgcolor("green")
wn.setup(width = 1080, height = 720)
wn.tracer(0)

# Scibe
Scribe = turtle.Turtle()
Scribe.speed(0)
Scribe.color("white")
Scribe.penup()
Scribe.hideturtle()
Scribe.goto(0, 310)
Scribe.write("Bears: 0 Tigers: 0", align = "center", font =("Courier", 24, "normal"))

# Score

ScoreA = 0
ScoreB = 0

# Keeper A
KeeperA = turtle.Turtle()
KeeperA.speed(0)
KeeperA.shape("square")
KeeperA.color("brown")
KeeperA.shapesize(stretch_wid = 3, stretch_len = .5)
KeeperA.penup()
KeeperA.goto(-500, 0)

# Keeoer A Functions
def KeeperA_up():
    yCor = KeeperA.ycor()
    yCor += 30
    KeeperA.sety(yCor)

def KeeperA_down():
    yCor = KeeperA.ycor()
    yCor -= 30
    KeeperA.sety(yCor)

# Keeper B
KeeperB = turtle.Turtle()
KeeperB.speed(0)
KeeperB.shape("square")
KeeperB.color("orange")
KeeperB.shapesize(stretch_wid = 3, stretch_len = .5)
KeeperB.penup()
KeeperB.goto(500, 0)

# Keeoer B Functions
def KeeperB_up():
    yCor = KeeperB.ycor()
    yCor += 30
    KeeperB.sety(yCor)

def KeeperB_down():
    yCor = KeeperB.ycor()
    yCor -= 30
    KeeperB.sety(yCor)


# Keeper commands
wn.listen()
wn.onkeypress(KeeperA_up, "w")
wn.onkeypress(KeeperA_down, "s")

wn.onkeypress(KeeperB_up, "Up")
wn.onkeypress(KeeperB_down, "Down")

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("black")
Ball.penup()
Ball.goto(0, 0)
Ball.shapesize(stretch_wid = .8, stretch_len = .8)
Ball.dx = .5
Ball.dy = .5




# Main game Loop
while (ScoreA < 4) or (ScoreB < 4):
    wn.update()

    # Ball Bounce

    # Ball tip off
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Ball Out of Bounds
    if Ball.ycor() > 350:
        Ball.sety(350)
        Ball.dy *= -1

    if Ball.ycor() < -350:
        Ball.sety(-350)
        Ball.dy *= -1


    if Ball.xcor() > 530:
        Ball.goto(0, 0)
        Ball.dx *= -1
        ScoreA += 1
        Scribe.clear()
        Scribe.write("Bears: {} Tigers: {}".format(ScoreA, ScoreB), align = "center", font =("Courier", 24, "normal"))

    if Ball.xcor() < -530:
        Ball.goto(0, 0)
        Ball.dx *= -1
        ScoreB += 1
        Scribe.clear()
        Scribe.write("Bears: {} Tigers: {}".format(ScoreA, ScoreB), align = "center", font =("Courier", 24, "normal"))

    # Ball blocked
    if (Ball.xcor() > 490 and Ball.xcor() < 500) and ((Ball.ycor() < KeeperB.ycor() + 30) and (Ball.ycor() > KeeperB.ycor() - 30)):
        Ball.setx(490)
        Ball.dx *= -1

    if (Ball.xcor() < -490 and Ball.xcor() > -500) and ((Ball.ycor() < KeeperA.ycor() + 30) and (Ball.ycor() > KeeperA.ycor() - 30)):
        Ball.setx(-490)
        Ball.dx *= -1
