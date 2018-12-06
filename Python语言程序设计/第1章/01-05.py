# -*- encoding: utf-8 -*-
'''
    draw OlympicSymbol
'''

import turtle

turtle.color('blue')
turtle.penup()
turtle.goto(-105, 0)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.color('black')
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.color('red')
turtle.goto(105, 0)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.color('yellow')
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.color('green')
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, 150)
turtle.pendown()
turtle.write('draw OlympicSymbol')
turtle.done()