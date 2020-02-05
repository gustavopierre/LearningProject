nota = input('Digite a nota do aluno: ')

if float(nota) >= 9:
    print("Quadro de Honra")
elif float(nota) >= 7:
    print("Aprovado")
elif float(nota) >= 5:
    print("Recuperação")
elif float(nota) >= 3:
    print("Recuperação + Trabalho")
else:
    print("Reprovado")
