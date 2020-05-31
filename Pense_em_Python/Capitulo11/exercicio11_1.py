import pprint

fin = open('./Capitulo9/words.txt')
words = dict()
for line in fin:
    word = line.strip()
    words[word] = 1


#pprint.pprint(words)

print('clear' in words)
