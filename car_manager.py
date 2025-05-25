from turtle import Turtle
import random

COLORS = ["hotpink", "thistle", "skyblue", "plum", "MistyRose2", "PaleGreen1", "LightSkyBlue3", "LightSteelBlue2", "PaleTurquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_x = 0.1
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # 20x40 px
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=random.randint(300, 500), y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def moving(self):
        """Car moves from the right to the left edge of the screen."""
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT+self.speed_x)

    def increase_speed(self):
        """Increase the speed of the car."""
        self.speed_x += 1