from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:  # 為什麼要這個才有畫面
    screen.update()
    time.sleep(0.05)
    snake.move()

    # eat
    if snake.head.distance(food) < 15.7:
        food.refresh()
        snake.extend_segment()
        # scoreboard.score += 1 Why it doesn't increase the score
        scoreboard.increase_score()

    # hit the wall
    if snake.head.xcor() < -290.5 or snake.head.xcor() > 290.5 or snake.head.ycor() < -290.5 or snake.head.ycor() > 290.5:
        food.hideturtle()  # # not working
        game_is_on = False
        scoreboard.game_over()

    # eat its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
