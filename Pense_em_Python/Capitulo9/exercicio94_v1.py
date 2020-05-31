def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


list = ['a', 'b', 'c', 'e']
fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, list):
        print(word)
fin.close()
