def has_duplicates(t):
<<<<<<< HEAD
    s = t[:]
    s.sort()

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
        
    return False


t = [8, 7, 6, 1, 2, 3, 4, 5, 6]
=======
    
    for elem in t:
        before = elem
        if before == elem:
            return True
    return False


t = [1, 2, 3, 4, 5, 6]
>>>>>>> 33330fc2c27a9e69f7936b6683dc0f9c30e88e85
print(has_duplicates(t))
