import turtle
t = turtle.Turtle()
s = turtle.Screen()


def fwd():
    t.forward(10)


def bwd():
    t.backward(10)


def counter_clock():
    t.left(10)


def clockwise():
    t.right(10)


def up():
    t.penup()


def down():
    t.pendown()


s.title("Halka majak")
s.screensize(500, 500)
t.shape("turtle")
s.listen()
s.onkey(fwd, "w")
s.onkey(bwd, "s")
s.onkey(counter_clock, "a")
s.onkey(clockwise, "d")
s.onkey(up, "u")
s.onkey(down, "i")
s.exitonclick()
