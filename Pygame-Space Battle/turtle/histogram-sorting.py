
#HOSTOGRAM ANIMATING TO MAKE ALL HISTOGRAM BLOCKS IN PRECEDING SEQUENCE

import turtle

T = turtle.Turtle()
T.hideturtle()
# turtle.tracer(0,0)
T.speed(0)
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


def drawBar(x, y):
    T.penup()
    # T.color(   gradecolor(y)    )
    T.begin_fill()
    T.setpos(x * xzoom, 0)
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

