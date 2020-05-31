def nested_sum(t):
    total = 0
    for nested in t:
        if type(nested) is list:
            total += sum(nested)
        elif type(nested) is int or type(nested) is float:
            total += nested
    return total

t=[[1, 2], 4, [5, 6, 7], [8], 9, [10, 11, 12]]
print(nested_sum(t))
