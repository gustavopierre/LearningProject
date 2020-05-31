#!/usr/bin/python3

with open('pessoas.csv') as arquivo:
    # acessa o arquivo a cada iteração, ou seja, realizando o streaming do arquivo
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado')
