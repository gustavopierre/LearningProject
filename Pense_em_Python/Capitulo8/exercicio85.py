def rotate_word(word, num):
    for c in word:
        # testa se a letra é maiúscula ou não
        if c.islower():
            last = 'z'
            first = 'a'
        else:
            last = 'Z'
            first = 'A'

        # obtendo a ordem da letra
        if ord(c) + num > ord(last):
            order = ord(first) + ord(c) + num - ord(last) - 1
        elif ord(c) + num < ord(first):
            order = ord(last) + (num + ord(c) - ord(first)) + 1
        else:
            order = ord(c) + num

        print(chr(order))


rotate_word('z', 1)
