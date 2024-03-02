from turtle import Screen
from paddle import Paddle
s = Screen()

s.bgcolor("black")
s.title("PONG")
s.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

s.listen()
s.onkey(right_paddle.go_up, "Up")
s.onkey(right_paddle.go_down, "Down")
s.onkey(left_paddle.go_up, "w")
s.onkey(left_paddle.go_down, "s")
s.setup(width=800, height=600)

game_is_on = True
while game_is_on:
    s.update()

s.exitonclick()
