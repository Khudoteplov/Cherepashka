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

turtle.speed(0)
for i in range (6):
    crc(10*i + 40, 10*i + 40, 0)
    crc(10*i + 40, -10*i - 40, 0)

turtle.getscreen()._root.mainloop()
