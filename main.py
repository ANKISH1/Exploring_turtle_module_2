import turtle
from turtle import Turtle, Screen
import random
# import villains

# print(heroes.gen())
# print(villains.gen())
#
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #final_color = (r, g, b)

    return r,g,b


tim = Turtle()

#
tim.shape("arrow")
tim.pensize(0)
# tim.color("red")
tim.speed(0)



def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random_color())
    draw_shape(i)

movement = [0, 90, 180, 360]

for i in range(100):
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(movement))


tim.penup()
tim.goto(-200, 300)
tim.pendown()


def draw_spirograph(certain_angle):
    for i in range(int(360/certain_angle)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + certain_angle)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()
