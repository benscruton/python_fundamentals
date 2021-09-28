def push_front(l, val):
    l.append(val)
    for i in range(len(l) - 1, 0, -1):
        l[i], l[i-1] = l[i-1], l[i]
    return l

x = [*range(1, 5)]
push_front(x, 0)
print(x)
push_front(x, -1)
print(x)