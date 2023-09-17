import turtle
import math

# Function to draw a point at the given (x, y) coordinates
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5)  

# Function to draw an ellipse using the polynomial method
def draw_ellipse(a, b):
    turtle.speed(2)  

    
    turtle.forward(a)
    turtle.backward(2 * a)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.backward(2 * b)
    turtle.forward(b)
    turtle.right(90)

    # Draw the ellipse using a polynomial approximation
    for i in range(0, 360, 5):
        x = a * math.cos(math.radians(i))
        y = b * math.sin(math.radians(i))
        draw_point(x, y)

    turtle.hideturtle()
    turtle.done()


a = 100  # Semi-major axis length
b = 50   # Semi-minor axis length

# Call the function to draw the ellipse
draw_ellipse(a, b)
