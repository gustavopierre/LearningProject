def histogram(s):
    d = dict()
    for c in s:
       d[c] = 1 + d.get(c, 0)
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse


h = histogram('Gustavo Moreira Pierre')
print(h)

print(invert_dict(h))
