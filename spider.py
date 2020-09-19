import turtle
import numpy as np

def spider(n,r):
    for i in range(n):
        turtle.goto(0,0)
        turtle.pendown()
        turtle.goto(r * np.cos(i * 360//n * np.pi/180), r * np.sin(i * 360//n * np.pi/180))
        turtle.stamp()
        turtle.penup()
 
spider(12, 300)

turtle.getscreen()._root.mainloop()
