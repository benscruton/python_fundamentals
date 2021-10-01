# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

# x = [-4, 1, 2, -4, -2]
# biggie_size(x)
# print(x)


# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(arr):
    if len(arr) < 1:
        return arr
    num_positives = 0
    for num in arr:
        if num > 0:
            num_positives += 1
    arr[-1] = num_positives
    return arr

# print(count_positives([-1,-2,-3,-4,-4,-3]))


# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sum_total(arr):
    total = 0
    for num in arr:
        total += num
    return total

# print(sum_total([]))            # 0
# print(sum_total([1, 2, 3, 4]))  # 10
# print(sum_total([4, 7, 8]))     # 19

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def avg(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)



# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    length = 0
    for _ in arr:
        length += 1
    return length



# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    if len(arr) < 1:
        return False
    mini = arr[0]
    for num in arr:
        if num < mini:
            mini = num
    return mini

print(minimum([-3,-6,-2]))



# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    if len(arr) < 1:
        return False
    maxi = arr[0]
    for num in arr:
        if num > maxi:
            maxi = num
    return maxi



# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def analyze(arr):
    if len(arr) < 1:
        return False
    total = 0
    minimum = arr[0]
    maximum = arr[0]
    length = 0
    for num in arr:
        length += 1
        total += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return {
        "sumTotal": total,
        "average": total / length,
        "nimimum": minimum,
        "maximum": maximum,
        "length": length,
    }


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1].

def reverse(arr):
    for i in range(len(arr) // 2):
        back = len(arr) - 1 - i
        arr[i], arr[back] = arr[back], arr[i]

x = [1,2,3,4,5]
y = [1,2,3,4,5,6]
z = []

print(x)
reverse(x)
print(x)
print()

print(y)
reverse(y)
print(y)
print()

print(z)
reverse(z)
print(z)
print()