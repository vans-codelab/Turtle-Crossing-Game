from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.show_level = False
        # self.update_level()

    def update_level(self):
        """Update the level on the scoreboard."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align='left', font=FONT)

    def next_level(self):
        """Show next level on the scoreboard."""
        self.level += 1
        self.update_level()

    def game_over(self):
        """Show 'GAME OVER' to the user."""
        self.goto(0,0)
        self.write(arg="GAME OVER", align='center', font=FONT)
