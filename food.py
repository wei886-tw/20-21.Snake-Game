from turtle import Turtle, Screen
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5, 0.5)
        self.speed("fastest")
        
    def refresh(self):
        self.penup()
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

    def disappear(self):
        self.color('black')



# screen = Screen()
#
# food = Food()
#
# screen.exitonclick()
