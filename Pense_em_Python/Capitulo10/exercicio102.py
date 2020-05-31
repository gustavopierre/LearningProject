def cumsum(t):
    new_t = []

    for i in range(len(t)):
        new_t.append(sum(t[:i+1]))

    return new_t


t = [1, 2, 3, 4, 5, 6, 7, 8]
print(cumsum(t))
