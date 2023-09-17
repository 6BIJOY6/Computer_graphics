import turtle

# Create a Turtle object
t = turtle.Turtle()


t.speed(1)


t.penup()
t.goto(0, -100)  
t.pendown()


def draw_sector(radius, angle):
    t.begin_fill()
    t.forward(radius)
    t.left(90)
    t.circle(radius, angle)
    t.left(90)
    t.forward(radius)
    
    t.end_fill()


draw_sector(100, 90)


turtle.exitonclick()
