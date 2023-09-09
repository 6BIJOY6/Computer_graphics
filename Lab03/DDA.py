import turtle

def draw_line_DDA(x1, y1, x2, y2):
    
    turtle.speed(1)  
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    x_increment = dx / steps
    y_increment = dy / steps

    # Draw the line
    for _ in range(steps + 1):
        turtle.goto(round(x1), round(y1))
        x1 += x_increment
        y1 += y_increment
    
    
    turtle.exitonclick()


x1, y1 = -50, -50
x2, y2 = 50, 50

# Call the function to draw the line
draw_line_DDA(x1, y1, x2, y2)
