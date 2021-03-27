#PENTAGON
import turtle
t=turtle.Turtle()
t.circle(1,2,1)
t.seth(to_angle=180)   # SET TURTLE HEADING INTO GIVEN DIRECTOIN wrt ORIGIN
# t.setx(100)          # SET THE POSITION OF X CORDINATE LEAVING Y # t.goto(100,0) or t.setpos(100,0)       # MOVES or SET POSITION OF TURTLE TO GIVEN COORDINATE
# t.home()             # BRING INITIAL TURTLE TO THE STARTING POINT DRAWING UNNECESSARY LINE.

turtle.home()          # NEW TURTLE FROM STARTING POINT
turtle.right(79)
turtle.color("red")
turtle.fd(50)
turtle.dot(10, "blue") # POINT(SIZE,COLOUR) FORM WHERE YOU PUT IT
turtle.lt(60)          # CHANGE DIRECTION TO LEFT
turtle.fd(200)
turtle.done()          # TURTLE HAS DONE, NOW STOP WORKING

