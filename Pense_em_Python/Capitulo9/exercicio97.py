def is_tree_double_letters(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i + 1] == word[i]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
            count = 0
    
    return False


fin = open('./Capitulo9/words.txt')
for line in fin:
    word = line.strip()
    
    if is_tree_double_letters(word):
        print(word)
        
