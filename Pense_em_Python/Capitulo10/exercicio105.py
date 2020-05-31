def is_sorted(t):
    # before = t[0]
    # for elem in t:
    #     if before > elem:
    #         return False
    #     before = elem
    # return True
    return t == sorted(t)


t = [1, 2, 3, 8, 4, 6, 7]
print(is_sorted(t))
