import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(score.move_speed)
    screen.update()
    car.create_car()
    car.move_car()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        score.increase_score()
        car.level_up()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
