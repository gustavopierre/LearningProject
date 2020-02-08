#!/usr/bin/python3
import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome:{}, Idade: {}'.format(*pessoa))

if entrada.closed:
    print('Arquivo de leitura foi fechado')
