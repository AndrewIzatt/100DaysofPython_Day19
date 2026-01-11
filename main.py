import turtle as t
import random
is_race_on = False
screen = t.Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index_positions = [-70, -30, 10, 50, 90, 130]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_racers = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_index_positions[turtle_index])
    turtle_racers.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for racer in turtle_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if user_bet == winning_color:
                print(f"You won! The {winning_color} is the winner!")
            else:
                print(f"You lost! The {winning_color} is the winner!")
        distance = random.randint(0, 10)
        racer.forward(distance)











screen.setup(width=500, height=400)
screen = t.Screen()
screen.exitonclick()