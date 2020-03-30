import turtle
import math

def polygon(t, n, length):
    angle = 360/n
    for count in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    n = int(2*math.pi*r/10)
    polygon(t, n, 10)


bob = turtle.Turtle()
print(bob)
circle(bob, 200)

turtle.mainloop()
