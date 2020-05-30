def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


count_no_letters = 0
fin = open('./Capitulo9/words.txt')
letters = []
while True:
    letter = input('Digite uma letra proibida ou "done" para sair: ')
    if letter == 'done':
        break
    letters.append(letter)

for line in fin:
    word= line.strip()
    list = ['a', 'b', 'c']
    if avoids(word, letters):
        count_no_letters += 1

fin.close()
print(f'Quantidade de palavras sem as letras {letters} é {count_no_letters}')
