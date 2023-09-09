import turtle

def draw_circle(xc, yc, r):
    turtle.penup()
    turtle.goto(xc, yc - r)
    turtle.pendown()

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        # Plot the points in all eight octants
        plot_points(xc, yc, x, y)
        
        x += 1
        
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

def plot_points(xc, yc, x, y):
    turtle.penup()
    turtle.goto(xc + x, yc + y)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc - x, yc + y)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc + x, yc - y)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc - x, yc - y)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc + y, yc + x)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc - y, yc + x)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc + y, yc - x)
    turtle.pendown()
    turtle.dot()
    
    turtle.penup()
    turtle.goto(xc - y, yc - x)
    turtle.pendown()
    turtle.dot()

if __name__ == "__main__":
    # Set up the turtle
    turtle.speed(0)  # Fastest drawing speed
    turtle.bgcolor("white")
    
    # Circle parameters
    x_center = 0
    y_center = 0
    radius = 100
    
    # Draw the circle
    draw_circle(x_center, y_center, radius)
    
    # Keep the window open until manually closed
    turtle.mainloop()
