# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:09:08 2022

@author: Dhananjai sharma

"""
'''
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


import turtle
from turtle import Screen
from random import randint

turtle.setup(600, 600)
window = Screen()
window.bgcolor("pink")
t = turtle.Turtle()
t.color('white')
t.shape('turtle')
def RandomBullshitGo():
    for i in range(1, 100):
        t.goto(randint(-450,0),randint(0,450))
def quit():
    window.bye()
window.onkey(RandomBullshitGo, 'r')
window.onkey(quit, 'q')

window.listen()
window.mainloop()

'''

# tkinter
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.geometry('300x300')
window.title('GUI')

lable = ttk.Lable(window, text = 'hello world').pack()
    
window.mainloop()

