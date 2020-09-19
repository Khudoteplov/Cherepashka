import turtle 
import numpy as np

def spiral( a, phi, x=0, y=0):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    i=.0
    while (i< phi):
        i+=phi/100
        turtle.goto(a/2/np.pi *i *np.cos(i), a/2/np.pi * i * np.sin(i))

spiral(40, np.pi *8)
turtle.getscreen()._root.mainloop()
