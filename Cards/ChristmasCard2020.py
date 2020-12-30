#!/usr/bin/env python3

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
    framePen.down()
    framePen.begin_fill()
    framePen.forward(300)
    framePen.left(90)
    framePen.forward(450)
    framePen.left(90)
    framePen.forward(300)
    framePen.left(90)
    framePen.forward(450)
    framePen.end_fill()
    framePen.hideturtle()

def tree():
    treePen = turtle.Turtle()
    treePen.color("#000000", "#804000")
    treePen.pensize(5)
    treePen.speed(10)
    treePen.showturtle()

    # Positioning
    treePen.penup()
    treePen.right(90)
    treePen.forward(300)
    treePen.left(90)
    treePen.forward(150)
    treePen.left(90)
    treePen.forward(80)
    treePen.right(90)
    treePen.forward(20)
    treePen.left(90)

    # Begin drawing trunk
    treePen.down()
    treePen.begin_fill()
    for i in range(4):
        treePen.forward(40)
        treePen.left(90)
    treePen.end_fill()

    # Begin drawing leaves
    treePen.penup()
    treePen.color("#000000", "#006600")
    treePen.forward(40)
    treePen.right(90)
    treePen.backward(20)

    treePen.begin_fill()
    treePen.down()
    treePen.forward(100)
    for i in range(3):

        treePen.left(130)
        treePen.forward(60)
        treePen.right(130)
        treePen.forward(30)

    treePen.left(130)
    treePen.forward(112)
    treePen.left(100)
    treePen.forward(112)

    for i in range(3):

        treePen.left(130)
        treePen.forward(30)
        treePen.right(130)
        treePen.forward(60)

    treePen.left(130)
    treePen.forward(100)
    treePen.end_fill()
    treePen.hideturtle()

def ornaments():
    oPen1 = turtle.Turtle()
    oPen1.pensize(5)
    oPen1.speed(10)
    oPen1.showturtle()

    def setPenO(oPen):
        oPen.penup()
        oPen.right(90)
        oPen.forward(300)
        oPen.left(90)
        oPen.forward(150)
        oPen.left(90)
        oPen.forward(120)

    def drawO(up, side, oPen, color):
        setPenO(oPen)
        # randomNum = random.randint(1, 4)
        # if randomNum == 1:
        #     color = "#cc0000"
        # elif randomNum == 2:
        #     color = "#ffdb4d"
        # elif randomNum == 3:
        #     color = "#6666ff"
        # elif randomNum == 4:
        #     color = "#ff00ff"
        oPen.color(color)
        oPen.forward(up)
        oPen.right(90)
        oPen.forward(side)
        oPen.speed(10)
        oPen.down()
        oPen.begin_fill()
        for i in range(72):
            oPen.left(5)
            oPen.forward(0.4)
        oPen.end_fill()
        oPen.penup()
        oPen.home()


    # t1 = Thread(target=drawO, args=([25, -30, oPen1]))
    # t1.start()

    drawO(25, -30, oPen1, "#cc0000")
    drawO(27, 30, oPen1, "#ffdb4d")
    drawO(75, -20, oPen1, "#6666ff")
    drawO(75, 40, oPen1, "#cc0000")
    drawO(125, -15, oPen1, "#ffdb4d")
    drawO(110, 20, oPen1, "#6666ff")
    drawO(180, 0, oPen1, "#cc0000")


    oPen1.hideturtle()

def hangingDeco():
    hPen = turtle.Turtle()
    hPen.pensize(7)
    hPen.speed(10)
    hPen.showturtle()

    def lower(color, dist):
        hPen.color(color)
        hPen.penup()
        hPen.right(90)
        hPen.forward(300)
        hPen.left(90)
        hPen.forward(150)
        hPen.left(90)
        hPen.forward(120)

        hPen.left(90)
        hPen.forward(dist)
        hPen.right(165)
        hPen.down()

        for i in range(10):
            hPen.forward(16)
            hPen.left(3)

        hPen.penup()
        hPen.home()

    lower("#cc0000", 68)
    lower("#ffff4d", 78)

    def mid(color, dist):
        hPen.color(color)
        hPen.penup()
        hPen.right(90)
        hPen.forward(300)
        hPen.left(90)
        hPen.forward(150)
        hPen.left(90)
        hPen.forward(160)
        hPen.left(90)
        hPen.forward(dist)

        hPen.right(155)
        hPen.down()
        for i in range(10):
            hPen.forward(14)
            hPen.left(3)

        hPen.penup()
        hPen.home()

    mid("#ffff4d", 50)
    mid("#cc0000", 60)

    def higher(color, dist):
        hPen.color(color)
        hPen.penup()
        hPen.right(90)
        hPen.forward(300)
        hPen.left(90)
        hPen.forward(150)
        hPen.left(90)
        hPen.forward(210)
        hPen.left(90)
        hPen.forward(dist)

        hPen.right(155)
        hPen.down()
        for i in range(10):
            hPen.forward(12)
            hPen.left(3)

        hPen.penup()
        hPen.home()


    higher("#ffff4d", 50)
    higher("#cc0000", 40)

    hPen.hideturtle()

def star():
    starPen = turtle.Turtle()
    starPen.color("#000000", "#ffff4d")
    starPen.pensize(5)
    starPen.speed(10)
    starPen.penup()
    starPen.right(90)
    starPen.forward(300)
    starPen.left(90)
    starPen.forward(150)
    starPen.left(90)
    starPen.forward(80)
    starPen.right(90)
    starPen.forward(20)
    starPen.left(90)
    for i in range(4):
        starPen.forward(40)
        starPen.left(90)
    starPen.forward(40)
    starPen.right(90)
    starPen.backward(20)
    starPen.forward(100)
    for i in range(3):

        starPen.left(130)
        starPen.forward(60)
        starPen.right(130)
        starPen.forward(30)

    starPen.left(130)
    starPen.forward(122)
    starPen.right(130)
    starPen.left(90)
    starPen.forward(25)
    starPen.right(90)
    starPen.forward(13)

    angle = 140
    starPen.down()
    starPen.begin_fill()
    for i in range(5):
        starPen.forward(20)
        starPen.right(angle)
        starPen.forward(20)
        starPen.right(72 - angle)
    starPen.end_fill()

    starPen.color("#ffff4d")
    for i in range(5):
        starPen.penup()
        starPen.forward(27)
        starPen.down()
        starPen.forward(10)
        starPen.backward(10)
        starPen.up()
        starPen.backward(7)
        starPen.right(angle)
        starPen.forward(20)
        starPen.right(72 - angle)

    starPen.hideturtle()

def wishes():
    wishPen = turtle.Turtle()
    wishPen.color("#cc0000")
    wishPen.speed(10)
    wishPen.penup()
    wishPen.left(90)
    wishPen.forward(110)
    wishPen.right(90)
    wishPen.forward(150)
    wishPen.write("Merry Christmas!",align="center", font=("Comic Sans MS", 33, "normal"))
    wishPen.backward(150)
    wishPen.left(90)
    wishPen.backward(400)
    wishPen.right(90)
    wishPen.forward(150)
    wishPen.write("Happy New Year!",align="center", font=("Comic Sans MS", 33, "normal"))
    wishPen.hideturtle()

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

    framePen2.right(180)
    framePen2.down()
    framePen2.begin_fill()
    framePen2.forward(300)
    framePen2.right(90)
    framePen2.forward(450)
    framePen2.right(90)
    framePen2.forward(300)
    framePen2.right(90)
    framePen2.forward(450)
    framePen2.end_fill()
    framePen2.hideturtle()

def text():
    penText = turtle.Turtle()
    penText.penup()
    penText.color("#cc0000")
    penText.speed(5)
    penText.left(90)
    penText.forward(100)
    penText.right(90)
    penText.forward(30)
    penText.write("Dear Mom and Dad,", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(50)
    penText.left(90)
    penText.color("#008000")
    penText.write("Merry Christmas!", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(40)
    penText.left(90)
    penText.color("#cc0000")
    penText.write("Thank you for supporting", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(40)
    penText.left(90)
    penText.write("me this year!", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(40)
    penText.left(90)
    penText.write("Happy New Year!", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(60)
    penText.left(90)
    penText.color("#008000")
    penText.write("Love,", font=("Comic Sans MS", 20, "normal"))
    penText.right(90)
    penText.forward(30)
    penText.left(90)
    penText.color("#cc0000")
    penText.write("Ryan", font=("Comic Sans MS", 20, "normal"))
    penText.hideturtle()

def presents():
    presPen = turtle.Turtle()
    presPen.pensize(5)
    presPen.speed(10)
    presPen.showturtle()
    presPen.color("#e60000", "#ffff33")

    def setPres():
        presPen.penup()
        presPen.right(90)
        presPen.forward(300)
        presPen.left(90)
        presPen.forward(190)
        presPen.left(90)
        presPen.forward(80)
        presPen.right(90)

    setPres()
    presPen.down()
    presPen.begin_fill()
    for i in range(2):
        presPen.forward(48)
        presPen.left(90)
        presPen.forward(30)
        presPen.left(90)
    presPen.end_fill()
    presPen.left(90)
    presPen.forward(15)
    presPen.right(90)
    presPen.pensize(7)
    presPen.forward(48)
    presPen.backward(48)
    presPen.pensize(5)
    presPen.left(90)
    presPen.backward(15)
    presPen.right(90)
    presPen.penup()
    presPen.backward(120)
    presPen.color("#e60000" ,"#4d79ff")
    presPen.down()
    presPen.begin_fill()
    for i in range(2):
        presPen.forward(45)
        presPen.left(90)
        presPen.forward(30)
        presPen.left(90)
    presPen.end_fill()
    presPen.left(90)
    presPen.forward(15)
    presPen.right(90)
    presPen.pensize(7)
    presPen.forward(48)
    presPen.hideturtle()

frame()
wishes()
tree()
ornaments()
hangingDeco()
star()
presents()

moveOn = str(input("If you are ready to read the card then type y: "))
if moveOn == "y":
    frame()
    frame2()
    text()

wn.mainloop()
