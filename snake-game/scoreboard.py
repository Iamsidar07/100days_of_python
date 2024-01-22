from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1 and update scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Move scoreboard turtle to center and write GAME OVER."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Clear the turtle previous write and rewrite score."""
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
