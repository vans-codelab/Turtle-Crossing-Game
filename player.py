from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")  # size = 20x20 px
        self.color("DarkSeaGreen2")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Turtle moving forward by keypress."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Move turtle back to its starting position."""
        self.goto(STARTING_POSITION)