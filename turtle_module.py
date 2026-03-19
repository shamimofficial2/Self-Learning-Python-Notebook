import turtle as t

print("----------Graphic Open----------")

t.color("Red","White")
t.begin_fill()
t.speed(5)
t.shape("turtle")
t.bgcolor("black")
t.title("Python Turtle Module")
t.pensize(2)

print("----------Drow Starting----------")

t.forward(200)

t.dot()

t.left(90)
t.forward(200)

t.dot()

t.left(135)
for i in range(13):
    t.forward(19)
    t.penup()
    t.forward(3)
    t.pendown()

t.dot()

t.hideturtle()
t.clear()
t.showturtle()
t.right(225)

t.dot()

for i in range(4):
    t.forward(200)
    t.left(90)
    t.dot()
t.hideturtle()

t.showturtle()
t.clear()

t.circle(100)
t.hideturtle()
t.clear()

t.dot()
t.goto(0,100)
t.dot()
t.goto(0,-100)
t.dot()
t.hideturtle()
t.clear()

t.write("Click The Window")

print("----------Drow End----------")

t.end_fill()
t.exitonclick()

print("----------Graphic Close----------")