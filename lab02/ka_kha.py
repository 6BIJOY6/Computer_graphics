import turtle

def draw_bangla_ka():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)

def draw_bangla_kha():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)

if __name__ == "__main__":
    turtle.speed(1)
    
    # Draw "ক" (Ka)
    draw_bangla_ka()
    
    # Move to draw "খ" (Kha)
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    
    # Draw "খ" (Kha)
    draw_bangla_kha()

    turtle.done()
