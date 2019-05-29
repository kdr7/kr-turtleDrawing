#calls turtle library
import turtle

#creates variable my_turtle
my_turtle = turtle.Turtle()

#creates a function with multiple arguments
def square(length, angle):
    #draws the square
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

#creates loop where the function will run 4 times, drawing four squares
for i in range(4):
    square(100, 90)
