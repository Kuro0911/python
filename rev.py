def solve():
    n = int(input())
    if n%2==0:  
        print('Even')
    else:
        print('Odd')

class Car:
    def __init__(self,name):
        self.name = name
    def move(self):
        print('move')
    def dont(self):
        print('dont move')

class aaa(Car):
    pass 
print("Hello World")
t = int(input())
while t!=0:
    solve()    
    t-=1
else:
    print('test cases over')

c = Car()
c.move()
