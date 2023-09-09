import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.title("Draw Line Using Equation")


pen = turtle.Turtle()
pen.speed(1)  

# Line equation: y = mx + b

m = 2  
b = 50 


x1 = -50
y1 = m * x1 + b
x2 = 50
y2 = m * x2 + b


pen.penup()
pen.goto(x1, y1)
pen.pendown()


pen.goto(x2, y2)


screen.exitonclick()
