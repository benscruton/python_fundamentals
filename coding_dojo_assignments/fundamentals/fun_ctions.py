# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

def odd_even(max):
  for i in range(1, max + 1):
    quality = "odd" if i % 2 else "even"
    print(f"Number: {i}.  This is an {quality} number.")

# odd_even(2000)


# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by a second argument.

def multiply(l, multiplier):
  return [item * multiplier for item in l]

# print(multiply([2,4,10,16], 5))


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:

# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def layered_multiples(l):
  return [ [1] * num for num in l ]

print(layered_multiples(multiply([2,4,5], 3)))