import turtle
import math


def arc(t, r, angle):
    n = int(2*math.pi*r/10)
    x = int(n*angle/360)
    for count in range(x):
        t.fd(10)
        t.lt(360/n)
    print(f'r = {r}')
    print(f'angle = {angle}')
    print(f'n = {n}')
    print(f'x = {x}')


bob = turtle.Turtle()
print(bob)
arc(bob, 100, 270)

turtle.mainloop()
