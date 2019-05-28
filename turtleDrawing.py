#calls turtle library
import turtle

#creates variable my_turtle
my_turtle = turtle.Turtle()

#creates a function
def square():
    #draws the square
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)

#calls function
square()
my_turtle.forward(100)
square()

