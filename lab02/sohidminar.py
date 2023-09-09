import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

if __name__ == "__main__":
    turtle.speed(1)
    turtle.bgcolor("white")

    # Draw the base rectangle (red part)
    draw_rectangle("red", -100, -200, 200, 100)

    # Draw the circle (white part)
    draw_circle("white", 0, 100, 50)

    # Draw the top triangle (green part)
    draw_triangle("green", -75, 200, 150)

    # Draw the top rectangle (green part)
    draw_rectangle("green", -35, 100, 70, 30)

    turtle.hideturtle()
    turtle.done()
