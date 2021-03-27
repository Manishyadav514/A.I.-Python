import turtle                  #Drawing tool
import math
zoom = 0.02
T = turtle.Turtle()            #Initiates turtle
T.hideturtle()                 #Hides turtle cursor
turtle.tracer(0,0)
T.penup()
for v in range(10000):
    x = v*math.cos(v)*zoom
    y = v*math.sin(v)*zoom
    T.setpos(x,y)
    T.pendown()
    T.dot(2)
    T.penup()
turtle.update()
turtle.done()
