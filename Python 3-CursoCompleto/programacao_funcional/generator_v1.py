#!/usr/bin/python3
def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))