#!/usr/bin/python3

try:
    arquivo = open('pessoas.csv')
    # acessa o arquivo a cada iteração, ou seja, realizando o streaming do arquivo
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado')
