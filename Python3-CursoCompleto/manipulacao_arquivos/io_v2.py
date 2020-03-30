#!/usr/bin/python3
arquivo = open('pessoas.csv')
#acessa o arquivo a cada iteração, ou seja, realizando o streaming do arquivo
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
arquivo.close()
