from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


def get_highscore():
    with open("highscore.txt") as file:
        highscore = file.read()
    return int(highscore)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.highscore = get_highscore()
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1 and update scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_highscore()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Move scoreboard turtle to center and write GAME OVER."""
    #     if self.score > self.highscore:
    #         self.highscore = self.score
    #     self.update_scoreboard()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        """Clear the turtle previous write and rewrite score."""
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def set_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))
