from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # font_turtle = Turtle("square")  # how to make a turtle object within self
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0  # this line has to be wrote before self.write cuz there's a variation
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        # self.write line seems to create a turtle object on top and a scoreboard in the middle

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)  # 192 8:42

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)








