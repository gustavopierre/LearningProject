def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    if len(word) == 0:
        return True
    else:
        if first(word) == last(word) and is_palindrome(middle(word)):
            return True
        else:
            return False


print(is_palindrome('a'))
