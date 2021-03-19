#!/usr/bin/env python3

import turtle

wn = turtle.Screen()

def frame():
    framePen = turtle.Turtle()
    framePen.color("#ff99cc", "#000000")
    framePen.pensize(5)
    framePen.speed(10)
    framePen.showturtle()

    framePen.penup()
    framePen.right(90)
    framePen.forward(300)
    framePen.left(90)
    framePen.forward(-70)
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
    wishPen.color("#ff0066")
    wishPen.pensize(5)
    wishPen.speed(10)
    wishPen.showturtle()

    wishPen.penup()
    wishPen.right(90)
    wishPen.forward(-125)
    wishPen.left(90)
    wishPen.forward(102.5)
    wishPen.write("Happy Birthday!", align='center', font=('floydian', 35))
    wishPen.hideturtle()

def soundPrism():
    prismPen = turtle.Turtle()
    prismPen.color("#ffffff")
    prismPen.pensize(7)
    prismPen.speed(10)
    prismPen.showturtle()

    prismPen.penup()
    prismPen.right(90)
    prismPen.forward(160)
    prismPen.left(90)
    prismPen.forward(-70)
    prismPen.left(20)
    prismPen.forward(10)
    prismPen.pensize(5)

    prismPen.down()
    prismPen.forward(130)
    prismPen.left(40)
    prismPen.forward(60)
    prismPen.right(120)
    prismPen.forward(135)
    prismPen.right(120)
    prismPen.forward(135)
    prismPen.right(120)

    prismPen.forward(70)
    prismPen.pensize(3)
    prismPen.right(30)
    prismPen.penup()
    prismPen.forward(7)
    prismPen.down()
    prismPen.color("#cccccc")
    prismPen.begin_fill()
    prismPen.forward(40)
    prismPen.right(100)
    prismPen.forward(20)
    prismPen.right(110)
    prismPen.forward(40)
    prismPen.end_fill()
    prismPen.penup()
    prismPen.forward(7)
    prismPen.down()
    prismPen.left(240)

    prismPen.pensize(3)
    prismPen.color("#ffffff")
    prismPen.forward(65)
    prismPen.right(120)
    prismPen.forward(45)

    # Red
    prismPen.pensize(5)
    prismPen.color("#ff0000")
    prismPen.left(47)
    prismPen.penup()
    prismPen.forward(5)
    prismPen.down()
    prismPen.forward(155)
    prismPen.forward(-155)
    prismPen.right(90)
    prismPen.forward(5)
    prismPen.left(90.5)
    prismPen.penup()
    prismPen.forward(3)
    prismPen.down()

    # Orange
    prismPen.color("#ff6600")
    prismPen.forward(153)
    prismPen.forward(-153)
    prismPen.right(90)
    prismPen.forward(5)
    prismPen.left(90)
    prismPen.penup()
    prismPen.forward(3)
    prismPen.down()

    # Yellow
    prismPen.color("#ffff1a")
    prismPen.forward(151)
    prismPen.forward(-151)
    prismPen.right(90)
    prismPen.forward(4.5)
    prismPen.left(90)
    prismPen.penup()
    prismPen.forward(3)
    prismPen.down()

    # Green
    prismPen.color("#4dff4d")
    prismPen.forward(148)
    prismPen.forward(-148)
    prismPen.right(90)
    prismPen.forward(4.8)
    prismPen.left(90)
    prismPen.penup()
    prismPen.forward(3.5)
    prismPen.down()

    # Blue
    prismPen.color("#1a8cff")
    prismPen.forward(145.5)
    prismPen.forward(-145.5)
    prismPen.right(90)
    prismPen.forward(2.5)
    prismPen.color("#bf80ff")
    prismPen.forward(2.1)
    prismPen.left(90)
    prismPen.penup()
    prismPen.forward(3.5)
    prismPen.down()

    # Purple
    prismPen.color("#bf80ff")
    prismPen.forward(142)
    prismPen.forward(-142)

    prismPen.hideturtle()





frame()
wishes()
soundPrism()

wn.mainloop()
