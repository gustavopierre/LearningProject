# testa a quantidade de argumento
# testa o tipo do argumento
# verifica se está na main
# verifica a letra correspondente a nota e exibe

import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print('É necessário informar a nota.')
    print('Sintaxe: {} <nota>'.format(sys.argv[0][92:]))


def calcula_conceito(nota):
    if nota >= 9.1 and nota <= 10:
        return('A')
    elif nota >= 8.1:
        return('A-')
    elif nota >= 7.1:
        return('B')
    elif nota >= 6.1:
        return('B-')
    elif nota >= 5.1:
        return('C')
    elif nota >= 4.1:
        return('C-')
    elif nota >= 3.1:
        return('D')
    elif nota >= 2.1:
        return('D-')
    elif nota >= 1.1:
        return('E')
    else:
        return('E-')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    '''
        if not sys.argv[1].isnumeric:
        print(TerminalColor.ERRO +
              'A  nota deve ser um valor numérico.' + TerminalColor.NORMAL)
        exit(errno.EINVAL)
    '''

    nota = sys.argv[1]
    if nota <= 10 and nota >= 0:
        conceito = calcula_conceito(nota)
        print(conceito)
    else:
        print('Nota Inválida')
