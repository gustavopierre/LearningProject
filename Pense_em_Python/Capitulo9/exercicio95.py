def uses_all (word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


list = ['a','b','d', 'e', 'o']
fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    if uses_all(word, list):
        print(word)

fin.close()
