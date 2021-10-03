import datetime

def sep(length = 30):
    print()
    print("*" * length)
    print()

def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def gen_list(length = 20, maximum = 100, minimum = 0):
    import random
    import math
    arr = []
    for _ in range(length):
        num = random.random()
        num = math.floor(num * (maximum - minimum))
        num = math.floor(num) + minimum
        arr.append(num)
    return arr

def bubble_sort(arr):
    completed = False
    while not completed:
        completed = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                completed = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        mindex = i
        for j in range(i, len(arr)):
            if arr[mindex] > arr[j]:
                mindex = j
        arr[i], arr[mindex] = arr[mindex], arr[i]

def worse_insertion_sort(arr):
    for i in range(1, len(arr)):
        belongs = i
        while belongs > 0 and arr[i] < arr[belongs - 1]:
            belongs -= 1
        j = i
        while j > belongs:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1      

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def combine_arrays(arr1, arr2):
    output = []
    while len(arr1) and len(arr2):
        if arr1[0] < arr2[0]:
            output.append(arr1.pop(0))
        else:
            output.append(arr2.pop(0))
    while len(arr1):
        output.append(arr1.pop(0))
    while len(arr2):
        output.append(arr2.pop(0))
    return output

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    output = []
    while len(left) and len(right):
        if left[0] < right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    while len(left):
        output.append(left.pop(0))
    while len(right):
        output.append(right.pop(0))
    return output




def partition_array(arr):
    pivot = arr[-1]
    i = j = 0
    while i < len(arr):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return j - 1

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    j = partition_array(arr)
    left = quick_sort(arr[:j])
    right = quick_sort(arr[j:])
    return [*left, *right]

x = gen_list()
y = [*x]
print(x)
x = quick_sort(x)
bubble_sort(y)
print(x)
print(y)
print("Matches" if x == y else "Does not match")



    
# test = gen_list(100)
# print(test)
# print()
# bubble_sort(test)
# print(test)

# sep()

# test = gen_list(100)
# print(test)
# print()
# selection_sort(test)
# print(test)

# test = gen_list(100)
# print(test)
# sep()
# insertion_sort(test)
# print(test)
# print(check_sorted(test))


# test = gen_list(100)
# test2 = [*test]
# print(test)
# sep()
# test = merge_sort(test)
# print(test)
# bubble_sort(test2)
# print(test2)
# print(test == test2)
# print(check_sorted(test))

# mTest = gen_list(5000)
# bTest = [*mTest]
# wiTest = [*mTest]
# iTest = [*mTest]
# sTest = [*mTest]

# mStart = datetime.datetime.now()
# mTest = merge_sort(mTest)
# mEnd = datetime.datetime.now()
# print(f"Merge sort took {(mEnd - mStart).microseconds / 1000} ms.")

# bStart = datetime.datetime.now()
# bubble_sort(bTest)
# bEnd = datetime.datetime.now()
# print(f"Bubble sort took {(bEnd - bStart).microseconds / 1000} ms.")

# iStart = datetime.datetime.now()
# insertion_sort(iTest)
# iEnd = datetime.datetime.now()
# print(f"Insertion sort took {(iEnd - iStart).microseconds / 1000} ms.")

# wiStart = datetime.datetime.now()
# worse_insertion_sort(wiTest)
# wiEnd = datetime.datetime.now()
# print(f"Worse insertion sort took {(wiEnd - wiStart).microseconds / 1000} ms.")


# sStart = datetime.datetime.now()
# selection_sort(sTest)
# sEnd = datetime.datetime.now()
# print(f"Selection sort took {(sEnd - sStart).microseconds / 1000} ms.")