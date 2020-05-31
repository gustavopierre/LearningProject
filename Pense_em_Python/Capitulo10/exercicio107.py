def has_duplicates(t):
    s = t[:]
    s.sort()

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
        
    return False


t = [8, 7, 6, 1, 2, 3, 4, 5, 6]
print(has_duplicates(t))
