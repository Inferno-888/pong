# Building Pong with Python project

import turtle
import winsound

difficultySpeed = input("What level are you? Easy(e) Intermediate(i) Hard(h) \n")
if difficultySpeed == "e":
    difficultySpeed = 0.1
elif difficultySpeed == "i":
    difficultySpeed = 0.3
else:
    difficultySpeed = 0.5

maxGoals = int(input("How many goals do you have to score to win a match? \n"))

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Scores
score1 = 0
score2 = 0

# PADDLE 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.color("white")
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)


# PADDLE 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.color("white")
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = difficultySpeed
ball.dy = difficultySpeed

# Functions


def paddle1_up():
    y = paddle1.ycor()
    y += 20
    if y <= 250:
        paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    if y >= -250:
        paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    if y <= 250:
        paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    if y >= -250:
        paddle2.sety(y)



# Add the event listeners

win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Main game loop

while True:
    win.update()

    # Move the Ball

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border Checking!

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        # score increases
        score1 += 1
        if score1 == maxGoals:
            print("Player 1 Wins!!!")
            exit()
        else:
            winsound.PlaySound("goal.wav", winsound.SND_ASYNC)
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        # score increases
        score2 += 1
        if score2 == maxGoals:
            print("Player 2 Wins!!!")
            exit()
        else:
            winsound.PlaySound("goal.wav", winsound.SND_ASYNC)
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # Paddle Collisions

    if ball.xcor() <= -340 and (ball.ycor() <= paddle1.ycor() + 50 and ball.ycor() >= paddle1.ycor() - 50) and ball.xcor() >= - 350:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("paddleCollision.wav", winsound.SND_ASYNC)

    if ball.xcor() >= 340 and (ball.ycor() <= paddle2.ycor() + 50 and ball.ycor() >= paddle2.ycor() - 50) and ball.xcor() <= 350:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("paddleCollision.wav", winsound.SND_ASYNC)
