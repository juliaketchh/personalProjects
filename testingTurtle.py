import turtle

def drawSquare(color, x, y):
    turt.color("black", color)
    turt.setposition(x,y)
    turt.begin_fill()
    turt.forward(10)
    turt.right(90)
    turt.forward(10)
    turt.right(90)
    turt.forward(10)
    turt.end_fill()


screen = turtle.getscreen()
turt = turtle.Turtle()

turtle.screensize(210, 210, "#cad9ee")
turtle.title("TXT blue hour minisode")
turtle.exitonclick()
turt.hideturtle()

drawSquare("black", -60.00, 60.00)
drawSquare("red", 90.00, 90.00)
