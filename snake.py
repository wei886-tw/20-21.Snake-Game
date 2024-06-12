from turtle import Turtle


STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # 啟用snake即產生蛇身
        self.head = self.segments[0]

    def create_snake(self):  # method
        for position in STARTING_POINT:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # 不用self的原因
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed(1)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())  # pos method comes from turtle class

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # 蛇身有多長移動幾次
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # heading == 前進方向
            self.head.setheading(UP)  # setheading == 改變前進方向

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
