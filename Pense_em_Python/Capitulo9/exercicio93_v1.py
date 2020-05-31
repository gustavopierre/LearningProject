def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


fin = open('./Capitulo9/words.txt')

for line in fin:
    word= line.strip()
    list = ['a', 'b', 'c']
    if avoids(word, list):
        print(word)

