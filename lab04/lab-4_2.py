import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the maximum speed

# Set the radius of the circle
radius = 100

# Draw the circle using trigonometric method
def draw_circle(radius):
    for angle in range(0, 360, 1):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y)

# Move the turtle to the starting position
t.penup()
t.goto(radius, 0)
t.pendown()

# Draw the circle
draw_circle(radius)

# Keep the window open until manually closed
turtle.done()
