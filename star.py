import turtle
import numpy as np

def star(n, k, r):
    turtle.penup()
    for i in range(1, n+2):
        
        turtle.goto(r* np.cos( 2* np.pi / n *i*k), r* np.sin( 2* np.pi / n *i*k))
        turtle.pendown()
        
star(11, 4,100)

turtle.getscreen()._root.mainloop()
