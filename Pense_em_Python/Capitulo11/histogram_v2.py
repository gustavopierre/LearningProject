def histogram(s):
    d = dict()
    for c in s:
       d[c] = 1 + d.get(c, 0)
    return d

def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('Gustavo Moreira Pierre')
print(h)
print(h.get('a','xxxx'))
print_hist(h)

for key in sorted(h):
    print(key, h[key])
