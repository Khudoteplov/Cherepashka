import turtle
turtle.shape('classic')
def square (x,y,a):
    turtle.penup()
    turtle.goto(x - a/2, y - a/2)
    turtle.pendown()
    for i in 0,2,3,4 :
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()\

    
for i in range(10, 110, 10):
    square(0, 0, i)

turtle.getscreen()._root.mainloop()
