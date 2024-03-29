#!/usr/bin/env python3

import math
import turtle

wn = turtle.Screen()

def frame():

    framePen = turtle.Turtle()
    framePen.color("#00004d", "#cce5ff")
    framePen.pensize(5)
    framePen.speed(10)
    framePen.showturtle()

    framePen.penup()
    framePen.right(90)
    framePen.forward(300)
    framePen.left(90)
    framePen.forward(-5)
    framePen.down()
    framePen.begin_fill()
    framePen.forward(345)
    framePen.left(90)
    framePen.forward(495)
    framePen.left(90)
    framePen.forward(345)
    framePen.left(90)
    framePen.forward(495)
    framePen.end_fill()
    framePen.hideturtle()

def wishes():
    wishPen = turtle.Turtle()
    wishPen.color("#000000")
    wishPen.pensize(5)
    wishPen.speed(10)
    wishPen.showturtle()

    wishPen.penup()
    wishPen.right(90)
    wishPen.forward(-105)
    wishPen.left(90)
    wishPen.forward(167.5)
    wishPen.write("HAPPY", align='center', font=('Linkin Park', 55))
    wishPen.right(90)
    wishPen.forward(80)
    wishPen.write("MOTHER'S", align='center', font=('Linkin Park', 55))
    wishPen.forward(80)
    wishPen.write("DAY!", align='center', font=('Linkin Park', 55))
    wishPen.hideturtle()

def linkinPark():
    linkinPen = turtle.Turtle()
    linkinPen.pensize(9)
    linkinPen.speed(5)
    linkinPen.penup()
    linkinPen.showturtle()

    linkinPen.right(90)
    linkinPen.forward(230)
    linkinPen.left(90)
    linkinPen.forward(167.5)
    for i in range(4):
        linkinPen.right(4)
        linkinPen.backward(5)

    linkinPen.down()
    for i in range(48):
        linkinPen.left(4)
        linkinPen.forward(5)
    linkinPen.left(70)
    linkinPen.forward(115)
    linkinPen.left(115)
    linkinPen.forward(92)
    linkinPen.left(120)
    linkinPen.forward(72.5)
    linkinPen.left(120)
    linkinPen.forward(105)

    linkinPen.right(90)
    for i in range(32):
        linkinPen.right(4)
        linkinPen.forward(5)

    linkinPen.hideturtle()

def frame2():
    framePen2 = turtle.Turtle()
    framePen2.color("#00004d", "#cce5ff")
    framePen2.pensize(5)
    framePen2.speed(10)
    framePen2.showturtle()
    framePen2.penup()

    framePen2.right(90)
    framePen2.forward(300)
    framePen2.left(90)
    framePen2.forward(-5)
    framePen2.down()
    framePen2.left(180)

    framePen2.down()
    framePen2.begin_fill()
    framePen2.forward(345)
    framePen2.right(90)
    framePen2.forward(495)
    framePen2.right(90)
    framePen2.forward(345)
    framePen2.right(90)
    framePen2.forward(495)
    framePen2.end_fill()
    framePen2.hideturtle()

def text():
    penText = turtle.Turtle()
    penText.penup()
    penText.color("#00004d")
    penText.speed(6)
    penText.right(90)
    penText.forward(-120)
    penText.left(90)
    penText.forward(-5)
    penText.forward(30)

    penText.write("Dear Mom,", font=("Verdana", 25, "normal"))
    penText.right(90)
    penText.forward(73)
    penText.left(90)
    penText.write("Happy Mother's Day!", font=("Verdana", 25, "normal"))
    penText.right(90)
    penText.forward(53)
    penText.left(90)
    penText.write("Thank you for helping", font=("Verdana", 25, "normal"))
    penText.right(90)
    penText.forward(53)
    penText.left(90)
    penText.write("me with school and Boy", font=("Verdana", 25, "normal"))
    penText.right(90)
    penText.forward(53)
    penText.left(90)
    penText.write("Scouts!", font=("Verdana", 25, "normal"))
    penText.right(90)
    penText.forward(120)
    penText.left(90)
    penText.write("Love,", font=("Verdana", 26, "normal"))
    penText.right(90)
    penText.forward(40)
    penText.left(90)
    penText.write("Ryan", font=("Verdana", 26, "normal"))
    penText.right(90)
    penText.forward(50)
    penText.left(90)

    penText.hideturtle()

frame()
wishes()
linkinPark()
moveOn = str(input("If you are ready to read the card then type y: "))
if moveOn == "y":
    frame()
    frame2()
    text()

wn.mainloop()
