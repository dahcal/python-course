"""
    Python3 program for drawing time tables / mandelbrot circles
    Written by Oscar Calisch
"""

from math import *
from turtle import Turtle, Screen

## Initially the idea of using the edgle length came from looking at the archimedes method for pi. 
## A reduced and less consuming method was then implemented.
## The program operated by first drawing a circle, followed by a polygon pass by the turtle, saving each point. 
## Lastly lines are drawn between the poins accoding to the multiplier

SCALE = 300             # Size of circle. Default = 300
POLYGON_SIDES = 52      # Sides of polygon / number of points. Default = 52
MULTIPLIER = 2          # The multiplier for the time table. In theory any should work. Default = 2
DEBUG = True            # Debug statement. Set to false for reduced console spam and reporting


point_coordinates = []        # Defining list for point coordinates

# Draws a circle at SCALE
def draw_circle(turtle):
    turtle.goto(0, -SCALE)
    turtle.pendown()
    turtle.circle(SCALE)
    turtle.penup()

# Draws the inscribed circle / polygon
def inscribe_circle(turtle, sides, edge_length):
    turtle.goto(0, -SCALE)
    turtle.setheading(0)
    turtle.left(180 / sides)
    turtle.pendown()
    for _ in range(sides):
        point_coordinates.append(turtle.pos())      # Note, each coodinate is added before moving, not after. This is to ensure home is added, not hardcoded
        turtle.dot()                                # Draws a dot before moving
        turtle.forward(edge_length)                 # Moves forward according to edge length
        turtle.left(360 / sides)                    # Turn the appropriate angle for the polygon
    turtle.penup()

# Side length of an equal sided polygon with given radius(r) and number of sides(n)
def polygon_side_outer(r, n):
    return 2 * r * sin(pi/n) / cos(pi/n)


# Draws lines between the poins according to MULTIPLIER
def line_draw(turtle, points, mult):
    turtle.up() 
    overflow = floor(len(points) / mult)
    ovflow_flag = 0

    if DEBUG:                                   # Debug statement
        print("overflow: ", overflow)

    for i in range(len(points)):
        turtle.up()                             # Redundant up command incase some other function didn't implement it
        turtle.goto(points[i])
        i_mult = i * mult  
        turtle.down()

        if DEBUG:                               # Debug statement
            print("")
            print("interation:", i)
            print("i_mult: ", i_mult)

        if (i_mult < len(points)-1):            # Error catching to prevent out of bounds once index multiplier (i_mult) goes out of list bounds
            turtle.goto(points[i_mult])

        elif (ovflow_flag != 0) and (i_mult < (len(points)*ovflow_flag)-1): # If the overflow flag has been set and i_mult is within bounds
            i_mult = i_mult - len(points)*ovflow_flag                       # In theory this is redundant, but when I was testing having it integrated into main lead to some weird behaviour
            turtle.goto(points[i_mult])

        else:                                   # If the list is out of bounds increment overflow flag
            ovflow_flag +=1
            i_mult = i_mult - len(points)*ovflow_flag
            turtle.goto(points[i_mult])
        turtle.up()                             # Closing up command. Both for this function, but also to ensure that it doesnt draw in following commands

        if DEBUG:
            print("ovflow_flag: ", ovflow_flag)

# Main loop
def main():
    yertle = Turtle()                           # Some name to identify the turtle. Shamelessly ripped from an online example
    yertle.penup()
    yertle.speed(0)                             # Max speed(0) to make the drawing faster
    
    draw_circle(yertle)                         # Draws a circle with the defined turtle
    
    inscribe_circle(yertle, POLYGON_SIDES, polygon_side_outer(SCALE, POLYGON_SIDES))    # Draws the inscribed polygon
    
    line_draw(yertle, point_coordinates, MULTIPLIER)        # Draws the lines between the points
    
    yertle.hideturtle()                         # Hides the turtle when the drawing is complete.
    
    if DEBUG:
        print("")
        print("point_coordinates: ")
        print(point_coordinates)                # Debug printout of coordinates
    
    Screen().exitonclick()

if __name__ == "__main__":
    main()