import turtle

u=turtle.Turtle()
u.speed(100)
for i in range(50):
    u.pencolor('blue')
    u.left(25)
    u.right(110)
    u.forward(70)
    u.left(200)
    u.circle(20)

for i in range(4):
    u.left(100)
    u.back(30)
    for i in range(50):
        u.left(25)
        u.right(110)
        u.forward(70)
        u.left(200)
        u.circle(20)



