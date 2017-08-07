import turtle
import sys

scn = turtle.Screen()
scn.setworldcoordinates(0,0,5000,5000)
scn.bgcolor('lightgreen')
t = turtle.Turtle()
t.color('blue')
t.speed(0)

#rule:  F (go forward)
#rule2:  + (go right 45)
#rule3:  - (go left 45)

#0: F
#1  +F--F+
#2: +(+F--F+)--(+F--F+)+ 
#3: .. 

t.up()
t.goto(2500,2500)
t.down()

def levyC(count):
    t.right(45)
    if (count > 0):
        levyC(count - 1)
    else:
        t.forward(10)
    t.left(45)
    t.left(45)
    if (count > 0):
        levyC(count - 1)
    else:
        t.forward(10)
    t.right(45)

levyC(10)