palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')

print('fim')

aprovados = {'Rafaela', 'Pedro', 'Renato', 'Maria'}
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# set
dias_semana = {'Domingo', 'Segunda', 'Terça', 
               'Quarta', 'Quinta', 'Sexta', 'Sábado'}

for dia  in dias_semana:
    print(f'Hoje é dia {dia}')

#tupla
dias_semana = ('Domingo', 'Segunda', 'Terça', 
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia  in dias_semana:
    print(f'Hoje é dia {dia}')