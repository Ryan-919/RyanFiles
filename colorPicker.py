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



def colors(x, y):
    color = turtle.Turtle()
    color.penup()
    color.backward(x)
    color.left(90)
    color.forward(y)
    color.right(90)


graph()
colors(300, 300)



wn.mainloop()
