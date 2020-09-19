import turtle
import numpy as np

def crcd(r, x=0, y=0, p1=0, p2=360):
    turtle.penup()
    i = p1
    while(i<=p2):
        if (i == p1):
            turtle.penup()
        turtle.goto(x+r* np.cos(2* np.pi *i/360), y+r * np.sin(2* np.pi * i/360))
        turtle.pendown()
        i += 1
    turtle.penup()
    
turtle.color('yellow')
turtle.begin_fill()
crcd(200)
turtle.end_fill()

turtle.color('blue')
turtle.begin_fill()
crcd(20, -80, 100)
turtle.end_fill()

turtle.color('blue')
turtle.begin_fill()
crcd(20, 80, 100)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 20)
turtle.color('black')
turtle.width(30)
turtle.pendown()
turtle.goto(0, -10)
turtle.penup()


turtle.color('red')
turtle.width(15)

crcd(120, 0, -20, -180, 0)


turtle.getscreen()._root.mainloop()
