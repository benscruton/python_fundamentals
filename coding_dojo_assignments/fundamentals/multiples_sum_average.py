# Assignment: Multiples, Sum, Average
# This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!


# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

def multiples_part_1():
  for i in range(1, 1001, 2):
    print(i)


# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

def multiples_part_2():
  for i in range(5, 1000001, 5):
    print(i)


def multiples_generic(first, last, divisor):
  for i in range(first, last + 1, divisor):
    print(i)

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

def sum(l):
  sum = 0
  for num in l:
    sum += num
  print(sum)


# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

def average(l):
  if len(l) == 0:
    return print("There are no items in this list, sorry")
  total = 0
  for num in l:
    total += num
  print(total / len(l))

average([])