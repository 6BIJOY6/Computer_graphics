import turtle
import math


screen = turtle.Screen()
screen.title("Trigonometric Ellipse")

t = turtle.Turtle()
t.speed(0)  


def draw_ellipse(a, b):
    t.penup()
    t.goto(a, 0)
    t.pendown()

    for angle in range(0, 360, 1):
        x = a * math.cos(math.radians(angle))
        y = b * math.sin(math.radians(angle))
        t.goto(x, y)


semi_major_axis = 100  # Major radius
semi_minor_axis = 50   # Minor radius

draw_ellipse(semi_major_axis, semi_minor_axis)


screen.exitonclick()
