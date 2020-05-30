
def is_palindrome(word):
    if len(word) == 0:
        return True
    
    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome('ossos'))
