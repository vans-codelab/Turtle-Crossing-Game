import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from intro import Intro

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn animation off

intro = Intro()
scoreboard = Scoreboard()
car_manager = CarManager()
player1 = Player()

screen.listen()
screen.onkey(fun=intro.close_intro, key="Return")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Show animation screen

    # Start game when the introduction screen is closed
    if intro.closed:

        # Show scoreboard
        if not scoreboard.show_level:
            scoreboard.update_level()
            scoreboard.show_level = True

        # Turtle is now allowed to move by keypress up
        screen.onkey(fun=player1.move_up, key="Up")

        # Create and move cars
        car_manager.create_car()
        car_manager.moving()

        # Detect collision with cars
        for car in car_manager.all_cars:
            if car.distance(player1) < 20:
                game_is_on = False
                scoreboard.game_over()

        # When player has reached the top of the screen, place turtle back to the beginning and start the next level
        if player1.ycor() >= 300:
            player1.go_to_start()
            scoreboard.next_level()
            car_manager.increase_speed()


screen.exitonclick()

