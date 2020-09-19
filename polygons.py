import turtle
import numpy as np

def plgn(n, r, x=0, y=0):
    turtle.penup()
    for i in range(n+1):
        if (i == 0):
            turtle.penup()
        turtle.goto(x+r* np.cos(2* np.pi /n*i), y+r * np.sin(2* np.pi /n*i))
        turtle.pendown()
    turtle.penup()

for i in range(3, 15):
    plgn(i, 25 * (i-1), 0, 0)
    
turtle.getscreen()._root.mainloop()
