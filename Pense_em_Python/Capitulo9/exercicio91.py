fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
