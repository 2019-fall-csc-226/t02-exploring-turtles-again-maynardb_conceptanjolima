######################################################################
# Author: Concepta Njolima,Ben Maynard
# Username: njolimac, Maynardb
#
# Assignment: T02: Exploring Turtles in Python
# Purpose: Draw two letters that represent our team.
#
######################################################################

import turtle  #importing the turtle class
wn = turtle.Screen()
# set the background color to blue
wn.bgcolor("blue")

# Assigning variables design, concepta and ben to the turtles
concepta = turtle.Turtle()
ben = turtle.Turtle()
design = turtle.Turtle()
frame = turtle.Turtle()

# Assigning turtle shape to turtle
concepta.shape("turtle")
ben.shape("turtle")

#Assigning color to the turtles
concepta.color("red")
ben.color("black")
frame.color("red")
# Choose a pen size and size
pen = 7
size = 1
concepta.pensize(pen)
ben.pensize(pen)
frame.pensize(10)
#Draw a background design

for i in range(130):
    design.stamp()             # Leave an impression on the canvas
    design.penup()
    design.speed(0)
    size = size + 2          # Increase the size on every iteration by 2
    design.forward(size)       # Move tess along
    design.right(56)           #  ...  and turn her

# draw the frame
frame.penup()
frame.forward(280)
frame.left(90)
frame.forward(280)
frame.pendown()
for k in range(4):
    frame.left(90)
    frame.forward(600)
# Draw the letters

concepta.penup()
concepta.left(90)
concepta.forward(100)
concepta.pendown()
concepta.left(90)
concepta.forward(100)
concepta.left(90)
concepta.forward(100)
concepta.left(90)
concepta.forward(100)
concepta.penup()

ben.penup()
ben.forward(100)
ben.left(180)
ben.forward(80)
ben.pendown()
ben.right(180)
ben.forward(80)
ben.left(90)
ben.forward(75)
ben.left(90)
ben.forward(150)
ben.left(90)
ben.forward(150)
ben.left(90)
ben.forward(150)
ben.left(90)
ben.forward(75)
ben.penup()









