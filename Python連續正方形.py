import turtle

def draw_multicolor_square(t, sz):
        for i in [ "hotpink","pink","hotpink","pink"]:
                t.color(i)
                t.forward(sz)
                t.left(100)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)

size = 20
john.penup()
john.goto(-300,50)
john.pendown()

for i in range(15):
        draw_multicolor_square(john, size)
        john.penup()
        john.forward(40)
        john.pendown()

window.exitonclick()
