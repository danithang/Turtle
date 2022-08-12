#####Turtle Intro######
import turtle
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("deep pink")
tim.shapesize(1, 1, 1)
tim.speed("fastest")
# change width of pensize
tim.pensize(2)
t.colormode(255)


tim.setheading(0)

# Challenge 1 - Draw a Square ############
for _ in range(4):
    tim.forward(100)
    tim.right(90)

# Challenge 2 - Draw a dashed line ##########
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# alternate way to draw a dashed line ###########
for _ in range(10):
    tim.forward(10)
    tim.color("white")
    tim.forward(10)
    tim.color("dark orchid")
    tim.forward(10)

# Challenge 3 - Draw different shapes in 1 go #########
for _ in range(3):
    tim.forward(50)
    tim.right(120)
for _ in range(4):
    tim.color("orange")
    tim.forward(50)
    tim.right(90)
for _ in range(5):
    tim.color("blue")
    tim.forward(50)
    tim.right(72)
for _ in range(6):
    tim.color("purple")
    tim.forward(50)
    tim.right(60)
for _ in range(7):
    tim.color("yellow")
    tim.forward(50)
    tim.right(51)
for _ in range(8):
    tim.color("green")
    tim.forward(50)
    tim.right(45)
for _ in range(9):
    tim.color("cornsilk")
    tim.forward(50)
    tim.right(40)
for _ in range(10):
    tim.color("red")
    tim.forward(50)
    tim.right(36)

# Teacher solution for Challenge #3 #######
# defining random color from a tuple of the number version of the colors and returning color_scheme in function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_scheme = (r, g, b)
    return color_scheme


# define different shapes and pass through num_sides
def different_shapes(num_sides):
    # have variable angle to divide 360 by however many sides are on shapes then move forward then angle
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(80)
        tim.right(angle)


# for loop used to define shape side in a range of 3(triangle) to 10 sided shape
for shape_side_n in range(3, 11):
    # calling the color method and passing a random color from color_sides list
    tim.color(random_color())
    different_shapes(shape_side_n)

# Challenge #4 random walk ########
# giving a list of of all directions a turtle can face
directions = [0, 90, 180, 270]


# for loop to get a range to tell turtle to how many steps to take, 100 is the number
# telling turtle to go forward 30 steps and using setheading to get the random choice on directions list and colors list
for _ in range(100):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())

# Challenge 5 make a spirograph #######
for _ in range(100):
    tim.forward(100)
    tim.right(100)
    tim.color(random_color())

for _ in range(100):
    tim.circle(100)
    tim.left(20)
    tim.color(random_color())

# Teachers solution for Challenge 5 #######
# defining size of gap by dividing 360 by size of gap and creating circles with 100 radius
# tim.setheading is used to set original heading 0.0 and adding size_of_gap(5)
# size_of_gap will tell the circles to stop drawing, it also gives it the tilt to draw each circle 5 degrees
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())


# calling function and outputting size_of_gap with 5
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
