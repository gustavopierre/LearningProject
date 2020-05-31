def has_duplicate(t):
    d = dict()
    for e in t:
        if e in d:
            return True
        d[e] = 1
    return False


t = [8, 7, 16, 1, 2, 3, 4, 5, 6]
print(has_duplicate(t))
