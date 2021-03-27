#++++++++++++ TURTLE ++++++++++++++++#





#############################
# TURTLE MODULE AND COADING
#####
import turtle
t=turtle.Turtle()
turtle.bgcolor("white")            # CHANGES BACKGROUND COLOUR
#t.pen(fillcolor="black", pencolor="red", pensize=1)
#t.pensize(10)                                # SIZE OF THE PEN
#t.pencolor("red") or t.color("red")          # COLOR OF THE PEN
t.goto(50,50)                      # goto(x, y) go to position (x, y)
t.dot(10, "blue")                  # POINT(SIZE,COLOUR) FORM WHERE YOU PUT IT
t.speed(1)                         # CONTROL SPEED OF TURTLE
t.fd(100)                          # MOVE FORWARD
t.undo()                           # UNDO THE PREVIOUS COMMAND
t.setx(100)                        # SET THE POSITION OF X CORDINATE LEAVING Y # t.goto(100,0) or t.setpos(100,0)
t.color('red')                     # TURTLE COLOR START FROM WHERE YOU PUT IT
t.bk(20)                           # MOVE BACK ON SAME PATH
t.rt(70)                           # CHANGE ANGLE TO RIGHT
t.fd(-200)                         # OPPOSITE DIRECTION OF REAL EXPECTATION
t.seth(to_angle=-90)               # SET TURTLE HEADING INTO GIVEN DIRECTOIN wrt ORIGIN
#t.home()                           # BRING INITIAL TURTLE TO THE STARTING POINT DRAWING UNNECESSARY LINE.
#t.clear()                          #clear the screen, but do not move the turtle
#t.reset()                          # clear the screen and move turtle to ‘home’ i.e. (0, 0)
#t.bye()                            #close the turtle-drawing window
turtle.done()
#####
from turtle import *
bgcolor("white")                 # CHANGES BACKGROUND COLOUR
#pen(fillcolor="black", pencolor="red", pensize=1)
#pensize(10)                                # SIZE OF THE PEN
#pencolor("red") or t.color("red")          # COLOR OF THE PEN
goto(50,50)                      # goto(x, y) go to position (x, y)
dot(10, "blue")                  # POINT(SIZE,COLOUR) FORM WHERE YOU PUT IT
speed(1)                         # CONTROL SPEED OF TURTLE
fd(100)                          # MOVE FORWARD
undo()                           # UNDO THE PREVIOUS COMMAND
setx(100)                        # SET THE POSITION OF X CORDINATE LEAVING Y # t.goto(100,0) or t.setpos(100,0)
color('red')                     # TURTLE COLOR START FROM WHERE YOU PUT IT
bk(20)                           # MOVE BACK ON SAME PATH
rt(70)                           # CHANGE ANGLE TO RIGHT
fd(-200)                         # OPPOSITE DIRECTION OF REAL EXPECTATION
seth(to_angle=-90)               # SET TURTLE HEADING INTO GIVEN DIRECTOIN wrt ORIGIN
#home()                           # BRING INITIAL TURTLE TO THE STARTING POINT DRAWING UNNECESSARY LINE.
#clear()                          #clear the screen, but do not move the turtle
#reset()                          # clear the screen and move turtle to ‘home’ i.e. (0, 0)
#bye()                            #close the turtle-drawing window
done()
#####
#screensize(width, height)               set the size of turtle-drawing window
#position()                              display the current location of turtle
#penup() or up()                         keep pen up (not on paper) i.e. do not draw
#pendown() or down()                     keep pen down (on paper) i.e. draw
#quit()                                  quit the Python shell
#t.end_fill()
#####



print("===================================")




#############################
# SQUARE FORMATION
#####

import turtle
T = turtle.Turtle()
T.speed(0)
for i in range(4):
    T.forward(100)
    T.right(90)
turtle.done()
# SQUIRAL-SPIRAL
from turtle import *
for i in range(200):
    fd(i)
    lt(93)
    fd(i)
#####



print("===================================")




#############################
#  CIRCLE
####
# CICLE HAVING LENGTH OF THE RADIUS AND ANGLE OF THE ARC
import turtle
t = turtle.Turtle()
t.circle(100,360)
turtle.done()
# SPIRAL
for i in range(50):
    t.circle(i,45)
turtle.done()
# CONCENTRIC CIRCLE
for j in range(100):
    t.pendown()
    t.circle(2*j)
    t.penup()
turtle.done()
# CONCENTRIC CIRCLE
for i in range(50):
    t.circle(10 * i)
    t.up()
    t.sety(-(10 * i) )
    t.down()
turtle.done()
# CIRCLE   WITH WHILE
while(count <100):
   turtle.forward(5)
   turtle.left(4)
   count = count + 1
turtle.done()
#####
# CIRCLE FLOWER
from turtle import *
circle_size = 100
for i in range(6):
    circle(circle_size)
    left(60)
####




print("===================================")



#############################
#  4.STAR HAVING PENTAGON
####
import turtle
T=turtle.Turtle()
T.speed(0)
#draw a star spiral and overlaping pentagon
for i in range(50):
   T.forward(50+5*i)
   T.right(144)
T.penup()     #to stop drawing
T.home()      #reach starting point and draw ongoing statement
T.pendown()       #start drawing
#To draw pentagon
for i in range(50):
   T.forward(50+5*i)
   T.right(72)
turtle.done()
#####



print("===================================")



#############################
# 5.OVERLAPPING SPIRAL
####
import turtle
T=turtle.Turtle()
T.speed(0)
#draw overlapping spiral
for i in range(360):
   T.forward(100+5*i)
   T.right(179)
turtle.done()
#####



print("===================================")




#############################
# 6.RECTANGULAR SPIRAL
####
import turtle
T=turtle.Turtle()
T.speed(30)
for i in range(0,100):
    i=i+1
    T.forward(i*10)
    T.right(90)
    T.forward(i*10)
    T.right(90)
turtle.done()
#####





print("===================================")





#############################
# #1.b COLOURFULL HISTOGRAM
#####
import turtle
T = turtle.Turtle()
T.hideturtle()
turtle.tracer(0, 0)
xzoom = 30
yzoom = 3
def gradecolor(x):
    c = 'green'
    if x <= 20:
        c = 'red'
    elif x <= 50:  # this implies if x>20 and x<=50:
        c = 'orange'
    elif x <= 80:  # this implies if x>50 and x<=80:
        c = 'yellow'
    return c
def drawHistogram(A):
    for i in range(len(A)):
        T.penup()
        T.setpos(i * xzoom, 0)
        T.pendown()
        T.setpos(i * xzoom, A[i] * yzoom)
        T.dot(xzoom // 2)
def drawBetterHistogram(Arr):
    for i in range(len(Arr)):
        T.penup()
        T.color(gradecolor(Arr[i]))
        T.begin_fill()
        T.setpos(i * xzoom, 0)
        T.pendown()
        T.setpos(i * xzoom, Arr[i] * yzoom)
        T.setpos(i * xzoom + xzoom // 2, Arr[i] * yzoom)
        T.setpos(i * xzoom + xzoom // 2, 0)
        T.setpos(i * xzoom, 0)
        T.end_fill()
def main():
    A = [37, 50, 25, 48, 2, 10, 88, 44, 33, 57, 60, 30, 99, 34, 12, 8, 50]
    drawBetterHistogram(A)
    # <=20 == Red
    # 21 to 50 == orange
    # 51 to 80 = yellow
    # >80 = green
main()
turtle.update()
turtle.done()
#####


print("===================================")




#############################
# 1.c SORTING HISTOGRAM ANIMATING TO MAKE ALL HISTOGRAM BLOCKS IN PRECEDING SEQUENCE
#####
import turtle
T = turtle.Turtle()
T.hideturtle()
# turtle.tracer(0,0)
T.speed(0)
xzoom = 10                                   # BREADTH OF THE BARS
yzoom = 1                                    # LENGTH OF THE BARS
def drawBar(x, y):
    T.penup()
    T.begin_fill()                            # TO FILL BAR WITH COLOUR
    T.setpos(x * xzoom,0 )
    T.pendown()
    T.setpos(x * xzoom, y * yzoom)
    T.setpos(x * xzoom + xzoom // 2, y * yzoom)
    T.setpos(x * xzoom + xzoom // 2, 0)
    T.setpos(x * xzoom, 0)
    T.end_fill()
def drawThing(Arr):
    for i in range(len(Arr)):
        drawBar(i, Arr[i])
def swap(Arr, i, g):
    # Swap elements at positions i and g
    # 1. Delete the old bars
    T.color("white")
    drawBar(i, Arr[i])
    drawBar(g, Arr[g])
    # 2. Actually swap the values
    Arr[i], Arr[g] = Arr[g], Arr[i]
    # 3. Draw the new bars
    T.color("black")
    drawBar(i, Arr[i])
    drawBar(g, Arr[g])
def selectionSort(Arr):
    for i in range(len(Arr)):
        # g = location of minimum element from i onwards
        g = i
        for j in range(i, len(Arr)):
            if Arr[g] > Arr[j]:
                g = j
        swap(Arr, i, g)
def main():
    A = [37, 50, 25, 48, 2, 10, 88, 44, 33, 57, 60, 30, 99, 34, 12, 8, 50]
    # <=20 == Red
    # 21 to 50 == orange
    # 51 to 80 = yellow
    # >80 = green
    drawThing(A)
    selectionSort(A)
    print(A)
main()
turtle.update()
turtle.done()
#####



print("===================================")




#############################
# 9.CAGE
#####
import turtle
t=turtle.Turtle()
t.speed(10)
for i in range(5):
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(100)
    t.right(90)
t.penup()
t.home()
t.pendown()
for i in range(5):
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.left(90)
t.penup()
t.home()
t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
#####



print("===================================")



#############################
# 10. PERFECT SPIRAL
#####
import turtle
t=turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.pencolor('yellow')
t.pensize(2)
for i in range(1000):
    t.forward(1)
    t.forward(0.01+0.1*i)
    t.right(18)
t.penup()
t.home()
turtle.done()

#####



print("===================================")





#############################
# COLOURFUL ILLUSSING TUNNEL
#####
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])                   # [x%6] 6 IS SAME AS THE NUMBER OF COLOUR IN THE LIST
    t.width(x/100 + 1)                        # TO INCREASE THE WIDTH OF THE PEN
    t.forward(x)
    t.left(59)
#####
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'orange',"black"]
for x in range(150):
    pencolor(colors[x % 6])
    width(x / 10 + 1)
    forward(x)
    left(59)
#####




print("===================================")




#############################
# DRAWING MANY SQUARE WITH SLIGHTLY ANGLE CHANGING
#####
import  turtle
t=turtle.Turtle()
for i in range(10):
     turtle.fd(50)
     turtle.lt(80)
for i in range(20):
     turtle.undo()  #ITS REVERSE THE PROCESS
t.hideturtle()
def draw_square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.color('green')
for i in range(360):
    draw_square()
    turtle.left(i)
turtle.done()
#####



print("===================================")




#############################
# NOT WORKING
#####
import  turtle
from turtle import Turtle, Screen
t=Turtle("turtle")
screen=Screen()
t.speed(-1)
def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.toward(x,y))
    t.goto(x,y)
    t.ondrag(dragging)
def clickright():
    t.clear()
def main():
    turtle.listen()
    t.ondrag(dragging)
    turtle.onscreenclick(clickright,3)
    screen.mainloop()
main()
#####



print("===================================")




#############################
# STAR
#####
from turtle import *
color('red', 'blue')
begin_fill()                    # START FILLING COLOUR
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:          #TO STOP IF TURTLE CUTS ITS OWN LINE
        break
end_fill()                      # END FILLING COLOUR
done()
#####



print("===================================")




#############################
# COMPASS
#####
from turtle import *
for angle in range(0, 360, 20):
    setheading(angle)
    fd(100)
    write(str(angle) + '*')
    backward(100)
#####



print("===================================")




#############################
# COMPASS
#####
