'''
UNIT 1:

Structured Programming Paradigm -  advantage and disadvantage

Introduction to Python - 
> Python is a popular Programming language
> Created by Guido van Rosssum in 1991
> Uses : web dev, software dev
> Maths, system scripting etc

Print Statement - 
> Syntax: print("abc")

Comments in python -
> Syntax: # This is a Comment 

If-else Statement -
> example : 
a = 200
b = 33
if b>a :
    print("b is grater than a")
elif a==b:
    print("a is equal to a")
else :
    print("a is greater than b")

Indentation -
> Python relies on indentation (white space at the beginning of the line) to define scope in the code like {} used in C and C++.

Python Function - 
> Function is a block of code which only runs when it is called
> Reusability feature is enable 
> You can pass data, known as parameters into a Function
> A function can return data as a result 

Creating a function - (declaration and definition)
> It is defined using keyword def 
  def my_function():
     print("Hello from function")

Calling a function - 
> To call a function, use the function name followed by paranthesis
  my_function()

Example - 
def my_function():
   print("SRMIST")
my_function()

output: 
SRMIST

Arguments in Function - 
> Arguments are specified after the function name within the parenthesis
Example: def my_function(fname):
           print(fname + "Watson")
        my_function("Emil")
        my_function("Tobias")
        my_function("Linus")
output:
Emil Watson
Tobais Watson
Linus Watson

No. of Argument in function:
> By default, a function must be called with the correct no. of arguments. That is if your 
function expects 2 arguments you have to call the function with 2 arguments, not same or not less 

Default Arguments:
> Function arguments acn have default values in python
> We can provide a default value to an argument using the assignment operator(=)
Example: 
def my_fun(name, msg = "Good morning"):
   print ("Hello," name +"," msg )
my_fun("kate")
my_fun("Bruce","How you doing?") 
Output:
Hello Kate, Good morning
Hello Bruce, How yo doing?

Arbitrary arguments:
> If you do not know how many functions will be passed in your function, add a * before the parameter
name in the function definition.
> Arbitrary arguments are often shortened to *args in Python document.
> The way the function will recieve a tuple of arguments and can access the items accordingly.
Example :
def fruits(*fnames):
   for fruit in fnames:
      print (fruit)
fruits("orange","Banana","apple")
Output:
orange
Banana
apple

Keyword Arguments:
> You can also send arguments with the syntax - key = value
> This way the order of arguments doesnt matter.
> The phase keyword arguments are often shortened to Kwargs in Python document.
Example : 
def my_fun(child3,child2,child1):
   print("the youngest child is "+ child3)
my_fun(child1 = "Emil", child2 = "Tobins", child3 = "Linus")
Output:
The youngest child is Linus

The pass Statement:
> function definitions cannot be empty, but for some reason if you have a function definition
with no context , put in the pass statement to avoi errors.
Example:
def my_fun():
   pass

Recursion Function:
> Python also accepts recursion. 



--------UNIT2--------   


Event driven Programming Paradigm:-

Event-driven Programming is a Programming paradigm in which the flow of the program is determined by 
events such as user actions(mouse click, key press, sensor outputs or message from other programs/threads).
This is the dominant paradigm used in graphical user interface and other applications (eg. Javascript web
applications) that are centered on performing certain actions in response to user input.

Overview: Because the program execution is determined by events, an event driven application is designed to detect 
events as they occur, and then deal with them using an appropriate event handling procedure. In an event-driven application
-> there is generally a main loop that listens for events.
-> then triggers a call back function where one of those events is detected.

> Virtually all object-oriented and visual languages suuport event driven Programming. Visual Basic, visual C++ and Java are
  example of such languages.
> A usual programming IDE such as VB.Net provides much of the code for detecting events automatically when a new application
  is created.
> The programmer can therefore concentrate on issues such as interface design, which involves adding control such as command 
  buttons, text boxes, and labels to standard forms. Once the user interface is substantially complete; the programmer can add
  event handling code to each control as required.

Each event handler is usually bound to a specific object orcontrol on a form.

> One of the fundamental ideas behind object-oriented programming is that of representing programmable entities as objects.
  An entity is the context could be literally anything with which the application is concerned. A program dealing with tracking
  the progress of customers order for a manufacturing company. For example: might involve objcts such as "customer", "order" and
  "order items".
                     
                              Get/Set
Data  |  [Properties] |     <----------->    |               
      |               |                      |
      |               |          Call        | 
  &   |  [Methods]    |     <----------->    |   Application
      |               |                      |
      |               |       Respond to     |
Code  |  [Events]     |     <----------->    |

Relation between an object and an application:-

Events: Events are often actions performed by the user during the execution of a program, but can also be
        1. messages generated by a peripheral device or system handler
        2. an interrupt generated by a peripheral device or a system handler
        3. if the user click on a button with a mouse or hits the enter key it generates an event
        4. if a file download completes it generates an event
        5. if there is a hardware or software event it generates an event

Dispatcher/Scheduler : The events are dealt with by a central event handler called dispatcher and scheduler that runs continously
in the background and waits for an event to occur.
When an event does occur the scheduler must determine the type of event and call the appropriate event handler to deal with it.
The information passed to the event handler by the scheduler will vary but will include sufficient information to allow the
the event handler to take any necessary action.

Event handler can be seen as small blocks of procedure code that deals with very specific occurence.
They usually produce a visual response to inform or direct the user and often change the system's state.
The state of the system encompasses both the data used by the system(eg the value stored in a database field), and the
state of the user interface itself(eg which on-screen object currently has the focus or the background color of a text box).

> The event handler may even trigger another event to occur that will cause a second event handler to be called ( to avoid the 
  infinite loop).
> Similarly, an event handler may cause any queued events to be discarded (eg click on quit button to terminate the problem).

                    Events
                      |
                      |
                  scheduler
                      |
        ______________|_______________               
       |              |               |
       |              |               |
    Event           Event           Event
  handler 1      handler 2.......handler 'n'

Relation between events, scheduler and event handler:-
> As it can be seen in the figure, the central element of the event driven application is a scheduler that recieves a stream of events 
  & passes each event to the relevant event handler.
> The scheduler will continue to remain active until it encounters an event.
> under certain circusmtances the scheduler may encounter an event for which it cannot assign an appropriate event handler.
> Depending on the nature of the event the scheduler can either ignore it raise an exception ('throwing' an exception).

Pseudo code:

do forever: //the main schedular loop
get input from input stream
if event type == End program:
quit     // break out of event loop
else if event type == event_01
call event handler for event_01 with event parameters
else if event type == event_02:
call event handler for event_02 with event parameters
.
.
.
else if event type == event_nm:
call event handler for event_nm with event parameters
else handle unrecognised event // ignore or raise exceptional handling
end loop

Keypress event in python:

import turtle
turtle.setup (400,500)   #determine window size
wn = turtle.Screen()     #get reference to window
wn.title("Handling Keypress in python")
wn.bgcolor("blue")       #set background color
t = turtle.Turtle()      #create out fav. turtle
t.color("black")
t.shape("turtle")

#next functions are our event handler

def move():
    t.forward(2)    #move 2 pixels forward

def turn_left():
    t.left(90)      #turn left by 90*

def exit():
    wn.bye()        #close down the turtle window

# these lines associate keypress to the handlers we have defined

wn.onKey(move,"Space")
wn.onKey(turn_left,"Left")
wn.onKey(exit,"q")

# if any of the key that we are monitoring is pressed and then, released, its handler will be called.

wn.listen()
wn.mainloop()


import turtle
t = turtle.Turtle()  
ts = t.getscreen()
t.shape("turtle")
t.color("yellow")
ts.bgcolor("black")

# associate key presses & event handler 

def move():
   t.forward(2)   #move 2 pixel forward
def turn_left():
   t.left(90)     #turn left to 90*
def turn_right():
   t.right(90)
def spin():
   for i in range(4):
      t.right(90)
def exit():
   ts.bye()

ts.onKey(move,"Space")
ts.onKey(turn_left,"Left")
ts.onKey(turn_right,"Right")
ts.onKey(spin,"S")
ts.onKey(exit,"q")

Mouse Event:- 
In mouse event handler, it needs two parameters to recieve x,y coordinate information.

eg:-

import turtle
turtle.setup (400,500)  
wn = turtle.Screen()     
wn.title("Handle Mouse clicks on window")
wn.bgcolor("purple")       
tess = turtle.Turtle()     
tess.color("light green")
tess.pensize(3)
tess.shape("Circle")

def hl(x,y):
    tess.goto(x,y) # goto allow us to move the turtle to an absolute coordinate position

wn.onclick(hl)
wn.mainloop()

Automatic events from a timer:-

The turtle module in python has a timer that can cause an event when its time is up.

import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("timer to get events")
wn.bgcolor("light green")
tess = turtle.Turtle()
tess.color("purple")

def hl():
   tess.forward(100)
   tes.left(56)
   wn.ontimer(hl,60)

hl()
wn.mainloop()

GUI in python:-
>TKinter commonly comes bundled with python using TK and pythons's standard GUI framework.
>It gives us an object oriented interface to the TK GUI toolkit.

import the tkinter mode 
        |
        |
Create GUI application min window
        |
        |
   Add widgets
        |
        |
Enter main event loop

Code1:
import tkinter
window = tKinter.tk()
#to rename the title of the window
window.title("GUI")
#pack is used to show the object in the window
label = tKinter.label
label = tKinter.label(window,text="Hello World").pack()
window.mainloop()

label:
I1 = label(window,text="event loop",font("Arial","Bold","50"))
I1 = grid(column = 0,rows = 0)

Code2:
import tkinter
window = tKinter.tk()
window.geometer("300*300")
window.title("Welcome")
label1 = Label(window, text = "Window to tKinter",
               fg = "blue", bg = "yellow", relief = "solid",
               font = ("arial",12,"bold")).pack()
button1 = Button(window,text="Demo",fg="white",bg="brown",
                 relief="Groove",font=("arial",12,"bold"))
button1.place(x=110,y=110)
window.mainloop()

Numpy:- Numerical python
Numpy is the fundamental package for scientific computation in python. It contains among other
thing:
> a powerful N-dimensionl array object (Mathematical & logical)
> sophisticted (broadcasting) functions
> tools for integrating C/C++ and fortran code
> useful liner algebra, Fourier transform and random number capabilities 
Numpy can also be used as an efficient multi-dimensional container of generic data Arbitrary data 
types can be defined.
Numpy is often used with packages like SciPy(scientific python) and Mat-plotlib(plotting library)

Example:

>import numpy as np 
 a = np.array([1,2,3]) #one dimensional array
 print(a)

Output: [1,2,3]

>import numpy as np 
 x = np.zeros((5.),dtype=np.int64) -----To avoid bit error you need to mention the bit type
 print(x)

Output: [0 0 0 0 0] 

>import numpy as np 
 x = np.ones(5) 
 print(x)

Output: [1. 1. 1. 1. 1.] 

>import numpy as np 
 x = [1,2,3]
 a=np.asarray(x) 
 print(a)

Output: error
To avoid this error you need to include ((x),dtype=object)

ALGOL (Algorithmic language):
It is a family of imperative computer programming language , originally developed in the mid 1950s
which greatly influenced many other languages & was the standard method for algorithm description used
by the Association of computing Machine(ACM) in textbooks and other academic sources for more than 30
years.
> It follow Procedural, imperative, structured paradigm.
> ALGOL introduced code blocks and the begin....end pairs for delimiting them.
> It was also the first langauge to implement nested function definition.
  Major specification : ALGOL 58, ALGOL 60, ALGOL 68

Elm: It is a domain-specific programming language for declartively web browser-based graphical user 
     interface. Elm is purely functional and developed with emphasis on usability, performance and robustness.
> It is a delightful langauge for reliable web apps.
> Elm is a functional language that compiles to Java script.
> It helps to develop websites and webapps.
> It has a strong emphasis on simplicity and quality tooling.


Javascript(JS): It is a interpreted programming language that is high level, often just-in-time compiled
                & multi paradigm.
It has:
> Curly Bracket syntax.
> dynamic typing
> prototype based object orientation
> first class functions

Paradigm followed by Javascript are event driven functional, imperative.
> Alongside HTML and CSS, Javascript is one of the core technologies of the world wide web.
> It enables interactive web pages & it is an essential part of web applications.

Imperative Programming Paradigm:
In Computer Science, It is a programming paradigm that uses statements to change a program's state.
It consists of commands for the computer to perform .
It focus on how:
             - Program state
             - Instructions to change program state.

                 ---------> yes -> Do {.....}
                /                             \
Do-> is it true                                 Stop
                \                             /
                 ---------> no -> Do {......}
       
'''
