def is_abecedarian(word):
    for i in range(0, len(word)-1):
        if word[i + 1] < word[i]:
            return False
    return True

count = 0
count_ord = 0
fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    count += 1
    if is_abecedarian(word):
        print(word)
        count_ord += 1
print("Existem {} palavras com letras em ordem alfabética de {} palavras no arquivo".format(count_ord, count))
