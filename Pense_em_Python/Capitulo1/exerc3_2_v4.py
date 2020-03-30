def do_four(f, d):
    do_twice(f, d)
    do_twice(f, d)


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
do_four(print_twice, 'spam3')
