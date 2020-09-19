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

def halfCircle(r):
	for i in range(200):
		turtle.forward(r)
		turtle.right(180.0/200.0)


# for i in range(7):
#    crcd(50, 90*i, 0, 0, 180)
#    crcd(5 , 90*i + 45, 0, -180, 0)
turtle.left(90)
for i in range(4):
    halfCircle(1.5)
    halfCircle(0.5)

turtle.getscreen()._root.mainloop()
