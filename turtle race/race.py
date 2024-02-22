import random
import turtle
s = turtle.Screen()
s.title("PATAN MULTIPLE CAMPUS ANNUAL RACE")
s.setup(width=1000, height=700)
user_bet = s.textinput(title="BAJI", prompt="SATTA LAGAUNUS")
is_race_on = False
colors = ["red", "green", "blue", "yellow", "orange", "violet", "indigo"]
y_coordinate = [-90, -60, -30, 0, 30, 60, 90]
all_turtle = []

for turtle_index in range(0, 7):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.setpos(-490, y_coordinate[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for single_turtle in all_turtle:
        if single_turtle.xcor() > 480:
            is_race_on = False
            winning_color = single_turtle.pencolor()
            single_turtle.hideturtle()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
                for single_turtle in all_turtle:
                    single_turtle.hideturtle()
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                for single_turtle in all_turtle:
                    single_turtle.hideturtle()
        random_distance = random.randint(0, 10)
        single_turtle.forward(random_distance)
t = turtle.Turtle()
t.hideturtle()
t.write(arg="The End", move=False, align='center', font=('Arial', 20, 'normal'))
s.exitonclick()

