from turtle import Turtle, Screen


class Food:

    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("blue")
        # wrong version
        # self.food = Turtle()
        # self.food = turtle.shape("circle")
        # self.food = turtle.color("blue")


blue_circle = Food()

screen = Screen()
screen.exitonclick()
