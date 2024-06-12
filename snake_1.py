from turtle import Turtle
import time


class SnakeScreen:
    def __init__(self):
        from turtle import Screen
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.tracer(0)
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.1)
        screen.exitonclick()


class Snake:
    def __init__(self):
        self_segments = []
        self_starting_point = [(0, 0), (-20, 0), (-40, 0)]
        for position in self_starting_point:
            self = Turtle()
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(1)
            self.goto(position)
            self_segments.append(self)


            for seg_num in range(len(self_segments) - 1, 0, -1):
                new_x = self_segments[seg_num - 1].xcor()
                new_y = self_segments[seg_num - 1].ycor()
                self_segments[seg_num].goto(new_x, new_y)
            self_segments[0].forward(20)
            self_segments[0].left(90)


