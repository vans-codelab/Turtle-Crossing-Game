from turtle import Turtle

FONT_TITLE = ("Arial", 16, "bold")
FONT = ("Arial", 15, "normal")

class Intro(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("LightSkyBlue3")
        self.goto(-250,150)
        self.show_intro()
        self.closed = False

    def show_intro(self):
        """Shows the introduction text to the user."""
        title = "Welcome to the Turtle Crossing Game!"
        self.write(arg=title, align='left', font=FONT_TITLE)
        self.goto(-250,-30)
        text = ("Help your turtle cross the road without getting hit!\n\n"
                "* You can only move upwards, but not downwards.\n"
                "* Beware: The cars are getting faster after each level!\n\n"
                "Press 'Enter' to start the game.")
        self.write(arg=text, align='left', font=FONT)

    def close_intro(self):
        """Removes the introduction text."""
        self.clear()
        self.closed = True