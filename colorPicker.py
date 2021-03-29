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
        graph.right(90)
        graph.forward(600)
        graph.backward(600)
        graph.left(90)
        graph.forward(60)

    graph.undo()
    graph.penup()
    graph.backward(620)
    graph.right(90)
    for i in range(10):
        graph.forward(60)
        graph.left(90)
        graph.penup()
        graph.forward(20)
        graph.down()
        graph.forward(600)
        graph.backward(600)
        graph.penup()
        graph.backward(20)
        graph.right(90)
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
# colors(4, 2, 5, 1, 5)
colors(4, 0, 5, 0, 5)
colors(5, 1, 3, 5, 5)
colors(6, 0, 0, 5, 5)
colors(7, 1, 0, 5, 5)
colors(10, 1, 1, 1, 25)


wn.mainloop()
