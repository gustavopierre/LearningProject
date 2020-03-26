import turtle

def polygon(t, n, length):
    angle = 360/n
    for count in range(n):
        t.fd(length)
        t.lt(angle)


bob = turtle.Turtle()
print(bob)
polygon(bob, 10, 70)

turtle.mainloop()
