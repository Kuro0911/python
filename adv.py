from ast import pattern
from asyncio.windows_events import NULL
from cgitb import small
from distutils.command.bdist_msi import PyDialog
import imp
import math
import multiprocessing
from re import X
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


import _thread
import time

def print_time(name, delay):
    count = 0
    while count < 10:
        time.sleep(delay)
        count += 1
        print(f"{name} : {time.ctime(time.time())}")

try: 
    _thread.start_new_thread(print_time, ('one' , 0, ))
    _thread.start_new_thread(print_time, ('two' , 1, ))
except: 
    print("nigga pause")

from multiprocessing import Process

def moj(x):
    for i in x:
        if i!=7:
            print(f'moj {i*i*i}')

def sui(x):
    for i in x:
        if i == 7:
            print(f'suiiiii')

if __name__ == '__main__':
    x = [7, 6, 7, 1, 2]
    p1 = Process(target=moj, args=(x,))
    p2 = Process(target=sui, args=(x,)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('done')


from multiprocessing import Process,Pipe
def saySui(con):
    con.send("suiiiiiiiiiiiiiiiiiii")
    con.close()
if __name__ == '__main__':
    Pcon,Ccon = Pipe()
    p = Process(target=saySui, args=(Ccon,))
    p.start()
    print(Pcon.recv())
    p.join()

from multiprocessing import Queue,Process

def Sui(x,q):
    for i in x:
        if i % 2 == 0:
            q.put('suii')

if __name__ == '__main__':
    q = Queue()
    x = [2, 3, 1, 2]
    p = Process(target=Sui, args=(x,q,))
    p.start()
    p.join()
    while q.qsize():
        print(q.get())


from multiprocessing import Pool

def cube(x):
    return x*x*x

if __name__ == '__main__':
    p = Pool(processes=4)
    x = [2,4,8,16]
    out = p.map(cube,x)
    print(f'out : {out}')



from threading import Thread

def square(X):
    for i in x:
        print(i*i)

if __name__ == "__main__":
    x = [1,2,3,4,3]
    t = Thread(target=square,args=(x,))
    t.start()
    t.join()



from concurrent import futures
import threading as t
import time
def sq(n):
    print('{}: sleeping {}'.format(
        t.current_thread().name,n)
    )
    time.sleep(n / 10)
    print('{}: done with {}'.format(
    t.current_thread().name,n))
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
res = ex.map(sq, range(5,0,-1))
print(f'out : {res}')


'''
