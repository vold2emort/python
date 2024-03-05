import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
s = turtle.Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("SNAKE")
# refresh rate of screen is controlled
s.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()

s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.down, key="Down")
s.onkey(fun=snake.right, key="Right")
s.onkey(fun=snake.left, key="Left")
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    # khana bhetney

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # screen baira gaye game over

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    # snake collide with itself
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

s.exitonclick()
