import turtle

def draw_circle(radius):
    turtle.speed(0)  # Set the drawing speed (0 is the fastest)
    x, y = 0, radius
    d = 3 - 2 * radius

    while x <= y:
        # Plot the points in all octants
        plot_points(x, y)
        if d <= 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

def plot_points(x, y):
    # Plot points in all octants
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(-x, y)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(x, -y)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(y, x)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(-y, x)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(y, -x)
    turtle.pendown()
    turtle.dot(5, "black")

    turtle.penup()
    turtle.goto(-y, -x)
    turtle.pendown()
    turtle.dot(5, "black")

# Set up the turtle window
turtle.title("Bresenham's Circle Drawing Algorithm")
turtle.bgcolor("white")
turtle.setup(width=800, height=800)
turtle.setworldcoordinates(-400, -400, 400, 400)

# Set the radius of the circle
radius = 100

# Draw the circle using Bresenham's Algorithm
draw_circle(radius)

# Keep the window open until manually closed
turtle.done()
