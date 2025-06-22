from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()