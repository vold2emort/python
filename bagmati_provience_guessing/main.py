import turtle
import csv
tur = turtle.Turtle()
score = 0
screen = turtle.Screen()
screen.title("Bagmati Provience")
image = "no_district.gif"
screen.addshape(image)
turtle.shape(image)

while score < 14:
    if score == 13:
        print("You won\nUnparalled General Knowledge")
        break

    answer_district = screen.textinput(title=f"{score}/13 District", prompt="Kun jilla ho?")
    answer_district = str(answer_district)
    with open("names.csv", 'r') as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            if row[0].lower() == answer_district.lower():
                tur.penup()
                tur.hideturtle()
                tur.color("black")
                tur.goto(float(row[1]), float(row[2]))
                tur.write(row[0])
                score += 1
                break

# def get_mouse_click_coor(x, y):
#    print([x, y])
#

# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
