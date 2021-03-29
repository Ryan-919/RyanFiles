#!/usr/bin/env python3

import math
import turtle

wn = turtle.Screen()

def graph():
    graph = turtle.Turtle()
    graph.speed(10)
    graph.penup()
    graph.forward(-310)
    graph.left(90)
    graph.forward(300)
    graph.right(90)
    graph.down()
    for i in range(11):

        graph.write(i,align="left", font=("Arial", 18, "normal"))
        graph.forward(60)

    graph.undo()
    graph.penup()
    graph.backward(620)
    graph.right(90)
    for i in range(10):
        graph.forward(60)
        graph.write(i+1,align="left", font=("Arial", 18, "normal"))

    graph.hideturtle()

def colors(y, r, g, b, m):
    turtle.colormode(255)
    color = turtle.Turtle()
    # color.showturtle()
    color.speed(10)
    color.penup()
    color.backward(310)
    color.left(90)
    color.forward(300)
    color.right(180)
    color.forward(60*y)
    color.left(90)
    color.down()
    for i in range(10):
        multiplier = m*(i+1)
        color.color(multiplier*r, multiplier*g, multiplier*b)
        color.begin_fill()
        for i in range(4):
            color.forward(60)
            color.left(90)
        color.end_fill()
        color.forward(60)
    color.hideturtle()

graph()
colors(1, 5, 0, 0, 5)
colors(2, 5, 2, 0, 5)
colors(3, 5, 5, 0, 5)
colors(4, 0, 5, 0, 5)
colors(5, 1, 4, 4, 5)
colors(6, 1, 3, 5, 5)
colors(7, 0, 0, 5, 5)
colors(8, 2, 0, 4, 5)
colors(9, 5, 1, 4, 5)
colors(10, 1, 1, 1, 25)

def giveColor(rowNumber, row, r, g, b, m):
    if rowNumber == row:
        for i in range(10):
            finalR = r*m*(i+1)
            finalG = g*m*(i+1)
            finalB = b*m*(i+1)
            value = "(" + str(finalR) + "," + str(finalG) + "," + str(finalB) + ")"

            def rgbToHEX(red, green, blue):
                unit1 = math.floor(red/16)
                unit2 = (red/16 - math.floor(red/16)) * 16
                unit3 = math.floor(green/16)
                unit4 = (green/16 - math.floor(green/16)) * 16
                unit5 = math.floor(blue/16)
                unit6 = (blue/16 - math.floor(blue/16)) * 16

                def convert(unit):
                    if unit==10:
                        unit = str(unit)
                        unit = "A"
                    elif unit==11:
                        unit = str(unit)
                        unit = "B"
                    elif unit==12:
                        unit = str(unit)
                        unit = "C"
                    elif unit==13:
                        unit = str(unit)
                        unit = "D"
                    elif unit==14:
                        unit = str(unit)
                        unit = "E"
                    elif unit==15:
                        unit = str(unit)
                        unit = "F"
                    return unit

                unit1 = convert(unit1)
                unit2 = convert(unit2)
                unit3 = convert(unit3)
                unit4 = convert(unit4)
                unit5 = convert(unit5)
                unit6 = convert(unit6)
                HEXCode = "#" + str(unit1) + str(unit2) + str(unit3) + str(unit4) + str(unit5) + str(unit6)
                HEXCode = HEXCode.replace(".0", '')
                return HEXCode

            HEXCode = rgbToHEX(finalR, finalG, finalB)
            print("Column "+ str(i+1) + ": " + value + " HEX: " + HEXCode)

for i in range(10):
    rowNumber = int(input("Row number? "))
    giveColor(rowNumber, 1, 5, 0, 0, 5)
    giveColor(rowNumber, 2, 5, 2, 0, 5)
    giveColor(rowNumber, 3, 5, 5, 0, 5)
    giveColor(rowNumber, 4, 0, 5, 0, 5)
    giveColor(rowNumber, 5, 1, 4, 4, 5)
    giveColor(rowNumber, 6, 1, 3, 5, 5)
    giveColor(rowNumber, 7, 0, 0, 5, 5)
    giveColor(rowNumber, 8, 2, 0, 4, 5)
    giveColor(rowNumber, 9, 5, 1, 4, 5)
    giveColor(rowNumber, 10, 1, 1, 1, 25)

wn.mainloop()
