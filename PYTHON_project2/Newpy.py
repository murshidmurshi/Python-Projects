import turtle
t=turtle.Turtle()


for e in range(50):
    t.speed(10)
    t.forward(100)
    t.right(100)
    t.circle(113)
    for i in range(3):
        t.circle(20)
        t.forward(10)
        for n in range(4):
            t.circle(10)
            t.forward(40)

