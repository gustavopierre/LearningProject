import turtle

def square(t):
    for count in range(4):
        t.fd(100)
        t.lt(90)


bob = turtle.Turtle()
print(bob)
square(bob)

turtle.mainloop()
