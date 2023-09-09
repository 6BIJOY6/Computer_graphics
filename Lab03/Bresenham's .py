import turtle

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        turtle.goto(x1, y1)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    turtle.goto(x2, y2)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()


x1, y1 = -50, -25
x2, y2 = 50, 80


draw_line(x1, y1, x2, y2)


turtle.done()
