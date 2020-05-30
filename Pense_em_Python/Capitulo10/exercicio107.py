def has_duplicates(t):
    
    for elem in t:
        before = elem
        if before == elem:
            return True
    return False


t = [1, 2, 3, 4, 5, 6]
print(has_duplicates(t))
