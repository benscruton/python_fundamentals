def sep(length = 30):
    print()
    print("*" * length)
    print()

def check_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True

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

def selection_sort(l):
    for i in range(len(l) - 1):
        mindex = i
        for j in range(i, len(l)):
            if l[mindex] > l[j]:
                mindex = j
        l[i], l[mindex] = l[mindex], l[i]


            
    
test = gen_list(100)
print(test)
print()
bubble_sort(test)
print(test)

sep()

test = gen_list(100)
print(test)
print()
selection_sort(test)
print(test)
