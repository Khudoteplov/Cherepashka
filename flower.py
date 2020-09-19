import turtle
import numpy as np

def crc(r, x=0, y=0):
    turtle.penup()
    n=200
    for i in range(n):
        if (i == 0):
            turtle.penup()
        turtle.goto(x+r* np.cos(2* np.pi /n*i), y+r * np.sin(2* np.pi /n*i))
        turtle.pendown()
    turtle.penup()
k=8
r=100
for i in range(k):
	crc(r, r * np.cos(2* np.pi /k*i), r * np.sin(2* np.pi /k*i))

turtle.getscreen()._root.mainloop()
