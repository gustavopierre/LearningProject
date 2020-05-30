def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    return word == word[::-1]


for i in range (100000, 999999):
    if is_palindrome(str(i)[2:]) and is_palindrome(str(i+1)[1:]) and is_palindrome(str(i+2)[1:5]) and is_palindrome(str(i+3)):
                    print(i)
