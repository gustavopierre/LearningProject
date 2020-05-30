def find(word, letter, first):
    index = first
    for w in word[first:]:
        if w == letter:
            return index
        index += 1 
    return -1


print(find('Gustavo', 'a', 3))
