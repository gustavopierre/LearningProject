import turtle

def square(t, length):
    for count in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
print(bob)
square(bob, 300)

turtle.mainloop()
