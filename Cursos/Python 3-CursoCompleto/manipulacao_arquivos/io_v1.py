#!/usr/bin/python3
arquivo = open('pessoas.csv')
# carrega o arquivo todo para a variável dados
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    # print(*registro.split(','))
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
