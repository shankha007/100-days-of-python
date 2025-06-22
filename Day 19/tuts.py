from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_win():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="c", fun=clear_win)

screen.exitonclick()