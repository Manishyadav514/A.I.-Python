#COLOURFULL HISTOGRAM

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

