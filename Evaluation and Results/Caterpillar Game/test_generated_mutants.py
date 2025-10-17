import pytest
from selected_functions import *
import turtle as t
import random as rd

@pytest.fixture(autouse=True)
def reset_state():
    import selected_functions
    if hasattr(selected_functions, 'game_started'):
        selected_functions.game_started = False  # Reset boolean flag, not a container

    # Reset turtle objects; handle cases where they may not be initialized
    if hasattr(selected_functions, 'caterpillar') and isinstance(selected_functions.caterpillar, t.Turtle):
        selected_functions.caterpillar.clear()
        selected_functions.caterpillar.hideturtle()
        selected_functions.caterpillar.penup()
        selected_functions.caterpillar.setpos(0, 0)
        selected_functions.caterpillar.setheading(0)
        selected_functions.caterpillar.shapesize(1, 1, 1)

    if hasattr(selected_functions, 'leaf') and isinstance(selected_functions.leaf, t.Turtle):
        selected_functions.leaf.clear()
        selected_functions.leaf.hideturtle()
        selected_functions.leaf.penup()
        selected_functions.leaf.setpos(0, 0)

    if hasattr(selected_functions, 'score_turtle') and isinstance(selected_functions.score_turtle, t.Turtle):
        selected_functions.score_turtle.clear()
        selected_functions.score_turtle.hideturtle()
        selected_functions.score_turtle.penup()
        selected_functions.score_turtle.setpos(0, 0)

    if hasattr(selected_functions, 'text_turtle') and isinstance(selected_functions.text_turtle, t.Turtle):
        selected_functions.text_turtle.clear()
        selected_functions.text_turtle.hideturtle()
        selected_functions.text_turtle.penup()
        selected_functions.text_turtle.setpos(0, 0)


def test_move_down():
    caterpillar.setheading(0)
    move_down()
    assert caterpillar.heading() == 270

    caterpillar.setheading(180)
    move_down()
    assert caterpillar.heading() == 270

    caterpillar.setheading(90)
    move_down()
    assert caterpillar.heading() == 90

    caterpillar.setheading(270)
    move_down()
    assert caterpillar.heading() == 270

def test_move_left():
    caterpillar.setheading(90)
    move_left()
    assert caterpillar.heading() == 180

    caterpillar.setheading(270)
    move_left()
    assert caterpillar.heading() == 180

    caterpillar.setheading(0)
    move_left()
    assert caterpillar.heading() == 0

    caterpillar.setheading(180)
    move_left()
    assert caterpillar.heading() == 180

def test_move_right():
    caterpillar.setheading(90)
    move_right()
    assert caterpillar.heading() == 0

    caterpillar.setheading(270)
    move_right()
    assert caterpillar.heading() == 0

    caterpillar.setheading(0)
    move_right()
    assert caterpillar.heading() == 0

    caterpillar.setheading(180)
    move_right()
    assert caterpillar.heading() == 180

def test_move_up():
    caterpillar.setheading(0)
    move_up()
    assert caterpillar.heading() == 90

    caterpillar.setheading(180)
    move_up()
    assert caterpillar.heading() == 90

    caterpillar.setheading(90)
    move_up()
    assert caterpillar.heading() == 90

    caterpillar.setheading(270)
    move_up()
    assert caterpillar.heading() == 270

def test_outside_window():
    window_width = t.window_width()
    window_height = t.window_height()

    # Inside the window
    caterpillar.setpos(0, 0)
    assert not outside_window()

    # On the left wall
    caterpillar.setpos(-window_width / 2 - 1, 0)
    assert outside_window()

    # On the right wall
    caterpillar.setpos(window_width / 2 + 1, 0)
    assert outside_window()

    # On the top wall
    caterpillar.setpos(0, window_height / 2 + 1)
    assert outside_window()

    # On the bottom wall
    caterpillar.setpos(0, -window_height / 2 - 1)
    assert outside_window()

    # Just inside the walls
    caterpillar.setpos(-window_width / 2 + 1, -window_height / 2 + 1)
    assert not outside_window()

    caterpillar.setpos(window_width / 2 - 1, window_height / 2 -1 )
    assert not outside_window()

def test_place_leaf():
    initial_x = leaf.xcor()
    initial_y = leaf.ycor()
    leaf.showturtle() # Make sure it's visible to start.
    place_leaf()
    assert leaf.xcor() != initial_x
    assert leaf.ycor() != initial_y
    assert -200 <= leaf.xcor() <= 200
    assert -200 <= leaf.ycor() <= 200
    assert leaf.isvisible() # Leaf should be shown