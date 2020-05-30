def has_no_e(word):
    if word.find('e') >= 0 or word.find('E') >= 0:
        return False
    return True


fin = open('./Capitulo9/words.txt')
count_no_e = 0
count = 0
for line in fin:
    count += 1
    word = line.strip()
    if has_no_e(word):
        print(word)
        count_no_e += 1
print("Porcentagem é {}%".format(count_no_e*100/count))
