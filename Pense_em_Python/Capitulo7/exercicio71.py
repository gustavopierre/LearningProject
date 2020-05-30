import math 

def mysqrt(a):
    # pegando o quadrado perfeito anterior ao número
    for i in range(1, int(a+1)):
        if i*i <= a:
            x = i*i
    while True:
        # print(x)
        y = (x + a/x)/2
        if y == x:
            break
        x = y
    return y


def test_square_root():
    print('a-      mysqrt      -   math.sqrt(a)    - diff')
    for a in range(1, 10):
        print(f'{a:^2}-{mysqrt(a):>18.16f}-{math.sqrt(a):>18.16f} - {mysqrt(a)-math.sqrt(a)}')
        #print('{}-{18.f}-{18.f}-{}'.format(a, mysqrt(a), math.sqrt(a), mysqrt(a)-math.sqrt(a)))


# print(mysqrt(121.4))
test_square_root()
