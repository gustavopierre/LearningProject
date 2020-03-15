def do_twice(f, a):
    f(a)
    f(a)


def print_twice(c):
    print(c)
    print(c)


def print_spam(b):
    print(b)


s = 'spam'
do_twice(print_spam, s)
do_twice(print_twice, "spam2")
