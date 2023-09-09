import turtle

# Function to draw letter "A"
def draw_A():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.left(75)
    turtle.forward(100)
    turtle.right(150)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(105)
    turtle.forward(35)

# Function to draw letter "B"
def draw_B():
    turtle.penup()
    turtle.goto(50, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(-50, 180)
    turtle.left(180)
    turtle.circle(-50, 180)
    turtle.right(90)
    turtle.forward(100)

# Main program
if __name__ == "__main__":
    turtle.speed(1)  # You can adjust the speed (1 = slowest, 10 = fastest)
    
    # Draw letter "A"
    draw_A()
    
    # Move to draw letter "B"
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    
    # Draw letter "B"
    draw_B()
    
    turtle.done()
