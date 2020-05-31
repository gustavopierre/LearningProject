t = []
fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    t.append(word)

fin.close()
print(t)
