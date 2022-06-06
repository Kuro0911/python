# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:09:08 2022

@author: Dhananjai sharma
"""

import turtle
from turtle import Screen
from random import randint
turtle.setup(400, 500)
window = Screen()
window.bgcolor('blue')
t = turtle.Turtle()
t.color('black')
t.shape('turtle')
def move():
    t.forward(10)
def turn_left():
    t.left(90)
def moj():
    t.goto(randint(-150,0),randint(0,150))
def exit():
    window.bye()
window.onkey(move, 'space')
window.onkey(turn_left, 'Left')
window.onkey(moj, 'Right')
window.onkey(exit, 'q')

window.listen()
window.mainloop()