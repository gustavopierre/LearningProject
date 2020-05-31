def histogram(s):
    d = dict()
    for c in s:
       d[c] = 1 + d.get(c, 0)
    return d


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('Value does not appear in the dictionary')


h = histogram('Gustavo Moreira Pierre')
print(h)

k = reverse_lookup(h, 5)
print(k)
