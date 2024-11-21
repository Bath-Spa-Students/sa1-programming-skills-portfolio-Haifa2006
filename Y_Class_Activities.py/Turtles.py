#Turle 1
import turtle
turtle.forward(50)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)

#Turtle 2
import turtle

# Set up the screen
screen = turtle.Screen()
 # Background color
screen.bgcolor("black")  

# Create a turtle named "spiral"
spiral = turtle.Turtle()
spiral.speed(0) 
spiral.width(2)  

# List of colors for the spiral
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

# Draw a colorful spiral
for i in range(360):
    spiral.pencolor(colors[i % 6]) 
    spiral.forward(i * 3 / 2 + i)  
    spiral.left(59) 

# Hide the turtle after drawing
spiral.hideturtle()

# Keep the window open until clicked
turtle.done()