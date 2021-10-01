# Countdown - Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countdown(start):
    return list(range(start, -1, -1))

# print(countdown(10))
# print(countdown(14))
# print(countdown(-0))


# Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.

def print_and_return(print_me, return_me):
    print(print_me)
    return return_me

# x = print_and_return("print this", "value of x")
# print(f"The value of x is:\n{x}")


# First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.

def first_plus_length(L):
    return L[0] + len(L)


# Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False

def values_greater_than_second(l):
    if len(l) < 2:
        return False
    output = []
    for item in l:
        if item > l[1]:
            output.append(item)
    return output

# print(values_greater_than_second([1,2,3,4,5]))
# print(values_greater_than_second([5,4,3,2,1]))
# print(values_greater_than_second([4,5,3,2,1]))



# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def length_and_value(size, value):
    output = []
    for _ in range(size):
        output.append(value)
    return output

seven_fours = length_and_value(7, 4)
print(seven_fours)
