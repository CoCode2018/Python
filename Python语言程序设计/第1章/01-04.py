# -*- encoding: utf-8 -*-

# improt turtle module
import turtle

turtle.showturtle()
turtle.write("Welcome to Python")
turtle.forward(100)
turtle.right(90)
turtle.color('red')
turtle.forward(50)
turtle.right(90)
turtle.color('green')
turtle.forward(100)
turtle.right(45)
turtle.forward(80)

# test2
import turtle

turtle.goto(0, 50)
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.color('red')
# Draw a circle with radius 50(半径50, 起点非圆形, 起点往上)
turtle.circle(50)