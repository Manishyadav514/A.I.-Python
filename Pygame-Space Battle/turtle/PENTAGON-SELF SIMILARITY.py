import turtle
import random
T= turtle.Turtle()
T.speed(0)
turtle.tracer(0,0)
T.penup()
T.hideturtle()
def halfway_there(a, b):
   x = (a[0]+b[0])/2
   y = (a[1]+b[1])/2
   return (x,y)
color = ['red','green','blue','yellow','black']
p = [None]*5
T.right(72)
T.setpos(100,300)         # TO FIX POSITION OF IMAGE
for i in range(5):
   T.forward(300)
   T.right(72)
   p[i] = T.pos()
   T.color(color[i])
   T.dot(5)
for i in range(10000):
   ##randomly choosing red, green, blue
   choice = random.randint(0,4)
   middle = halfway_there(T.pos(), p[choice])
   T.setpos(middle)           # FILLING POSITION OF OTHER POINTS DEFINED IN MIDDLE
   T.color(color[choice])     # FILLING COLOUR IN POINTS
   T.dot(6)
turtle.update()
turtle.done()
