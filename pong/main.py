from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
s = Screen()

ball = Ball()

s.bgcolor("black")
s.title("PONG")
s.tracer(0)
s.setup(width=800, height=600)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = ScoreBoard()
s.listen()
s.onkey(right_paddle.go_up, "Up")
s.onkey(right_paddle.go_down, "Down")
s.onkey(left_paddle.go_up, "w")
s.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_lpoint()
    if ball.xcor() < -380:
        ball.reset_position()
        score.add_rpoint()

s.exitonclick()
