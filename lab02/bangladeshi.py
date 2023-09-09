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

if __name__ == "__main__":
    turtle.speed(1)
    turtle.bgcolor("white")

    # Draw the green background
    draw_rectangle("#138808", -300, 200, 600, 400)

    # Draw the red circle
    draw_circle("red", -20, 0, 100)

    # Draw the circle inside the red circle
    

    turtle.hideturtle()
    turtle.done()
