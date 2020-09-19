import turtle
def sqrsp(n, a):
    for i in range(1, n):
        turtle.forward(a*i)
        turtle.left(90)

sqrsp(20, 30)
turtle.getscreen()._root.mainloop()


