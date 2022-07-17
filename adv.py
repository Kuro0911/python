from ast import pattern
from asyncio.windows_events import NULL
from cgitb import small
from distutils.command.bdist_msi import PyDialog
import math
'''
print('hello world')

a = int(input())
print(a*a*math.pi)
def si():
    P = int(input())
    IR = int(input())
    T = int(input())
    print(P*IR*T)

si()

a = int(input())
for i in range(1, a):
    for j in range(1 , i):
        print('*' , end="")
    print()

a = int(input())
fact = 1
for i in range(1 , a+1):
    fact *= i

print(fact)
class Node:
    def __init__(self , dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
class SingleLL:
    def __init__(self):
        self.headVal = None
    def print(self):
        val = self.headVal
        while val is not None:
            print(val.dataVal)
            val = val.nextVal

ll = SingleLL()
ll.headVal = Node(10)
l2 = Node(11)
l3 = Node(12)

ll.headVal.nextVal = l2
l2.nextVal = l3

ll.print()

import numpy as np
import cv2

filename = input( "Please enter filename: " )

img = cv2.imread( filename, -1 )

ROI_x, ROI_y = eval( input( "Enter (x, y) for ROI: " ) )
ROI_nr, ROI_nc = eval( input( "Enter (rows, columns) for ROI: " ) )
ROI = img[ ROI_x : ROI_x + ROI_nr, ROI_y : ROI_y + ROI_nc ]

cv2.imshow( "ROI", ROI )
cv2.imshow( "Example", img )
cv2.waitKey( 10000 )

cv2.destroyAllWindows() # work with cv2.waitKey(...)


from kanren import var,fact,run
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import associative, commutative

add = 'add'
mul = 'mul'

fact(commutative , add)
fact(commutative , mul)
fact(associative , add)
fact(associative , mul)

a,b,c = var('a') ,var('b'), var('c')
expr = (mul, (add , 1 , 2) , 4)
pat = (add , (mul , a , b) , c)

run(0, (a,b,c) , eq(expr, pat))

def sq(x):
    return x*x
def cube(x):
    return sq(x)*x
def ans(x, func):
    return func(x)
def hof(func1 , func2, x):
    return func1(x)*func2(x)

x = hof(cube,sq,2)
print(x)
'''
