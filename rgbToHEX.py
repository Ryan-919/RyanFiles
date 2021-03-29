#!/usr/bin/env python3

import math
import turtle

def rgbToHEX(red, green, blue):
    # red = int(input("Red value? "))
    # green = int(input("Green value? "))
    # blue = int(input("Blue value? "))

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

red1 = int(input("Red value? "))
green1 = int(input("Green value? "))
blue1 = int(input("Blue value? "))

HEXCode1 = rgbToHEX(red1, green1, blue1)
print(HEXCode1)

showcolor = str(input("Show color? "))
if showcolor == "y":
    wn = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(10)
    pen.color(HEXCode1)
    pen.begin_fill()
    for i in range(4):
        pen.forward(250)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()
    wn.mainloop()
