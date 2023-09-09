import turtle
import math

def draw_circle(radius):
    turtle.speed(0)  # Set the drawing speed to the fastest

    # Set the starting position to the first point on the circle
    x = radius
    y = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the circle using the parametric equation
    for theta in range(0, 360, 5):  # Increment angle in degrees
        x = radius * math.cos(math.radians(theta))
        y = radius * math.sin(math.radians(theta))
        turtle.goto(x, y)

    # Connect the last point to the starting point to complete the circle
    turtle.goto(radius, 0)

    turtle.done()

# Set the radius of the circle
radius = 100

draw_circle(radius)
