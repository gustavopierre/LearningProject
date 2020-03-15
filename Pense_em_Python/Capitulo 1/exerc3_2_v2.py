def do_twice(f, a):
    f(a)
    f(a)


def print_spam(b):
    print(b)


s = 'spam'
do_twice(print_spam, s)
