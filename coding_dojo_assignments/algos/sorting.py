def gen_list(length = 20, maximum = 100, minimum = 0):
    import random
    import math
    l = []
    for i in range(length):
        num = random.random()
        num = math.floor(num * (maximum - minimum))
        num = math.floor(num) + minimum
        l.append(num)
    return l

def bubble_sort(l):
    completed = False
    while not completed:
        completed = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                completed = False
                l[i], l[i+1] = l[i+1], l[i]
    
test = gen_list(10)
print(test)
bubble_sort(test)
print(test)
