import turtle as t

def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)

def move_counterclockwise():
    t.left(15)

def move_clockwise():
    t.right(15)

def clear_screen():
    t.resetscreen()

screen = t.Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_counterclockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()