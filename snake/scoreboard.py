import turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorebord()

    def update_scorebord(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases score"""
        self.score += 1
        self.update_scorebord()

    # same turtle is remodeled
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!!", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorebord()