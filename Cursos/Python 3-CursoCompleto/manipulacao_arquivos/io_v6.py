#!/usr/bin/python3

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        # acessa o arquivo a cada iteração, ou seja, realizando o streaming do arquivo
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo de leitura foi fechado')

if saida.closed:
    print('Arquivo de saída foi fechado')
