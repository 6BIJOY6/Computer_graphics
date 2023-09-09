import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_eye(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_smile(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(radius, 120)

if __name__ == "__main__":
    turtle.speed(1)
    
    # Draw the face
    draw_circle("yellow", 0, 0, 100)
    
    # Draw the eyes
    draw_eye("black", -35, 50, 15)
    draw_eye("black", 35, 50, 15)
    
    # Draw the smile
    draw_smile(-35, 20, 50)

    turtle.hideturtle()
    turtle.done()
