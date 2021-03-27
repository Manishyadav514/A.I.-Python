import turtle

T = turtle.Turtle()
T.hideturtle()
turtle.tracer(0, 0)
xzoom = 40
yzoom = 10

def drawBetterHistogram(A):
    for i in range(len(A)):
        T.penup()
        T.setpos(i * xzoom, 0)
        T.pendown()
        T.setpos(i * xzoom, A[i] * yzoom)
        T.setpos(i * xzoom + xzoom // 2, A[i] * yzoom)
        T.setpos(i * xzoom + xzoom // 2, 0)
        T.setpos(i * xzoom, 0)

def drawHistogram(A):
    for i in range(len(A)):
        T.penup()
        T.setpos(i * xzoom, 0)
        T.pendown()
        T.setpos(i * xzoom, A[i] * yzoom)
        T.dot(xzoom // 2)

def main():
    A = [37, 50, 25, 48, 2, 10, 88, 44, 33, 57]
    drawBetterHistogram(A) 
    #drawHistogram(A)

turtle.forward(300)
turtle.right(180)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
main()
turtle.update()
turtle.done()
