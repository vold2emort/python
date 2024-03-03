import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player_turtle = Player()

screen.listen()
screen.onkey(player_turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    scoreboard.display_level()
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player_turtle.is_at_finish():
        player_turtle.restore_position()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()
