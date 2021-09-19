# Assignment: Foo and Bar

# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

def find_square_root(num):
  half = midway = num // 2
  while half:
    square = midway * midway
    if square == num:
      return midway
    half //= 2
    midway += half if square < num else -half
  last_square = midway * midway
  midway += 1 if last_square < num else -1
  return midway if midway * midway >= num else midway + 1


def isPrime(num):
  if num == 2:
    return True
  sqrt = find_square_root(num)
  for i in range(2, sqrt + 1):
    if(num / i == num // i):
      return False
  return True

def isSquare(num):
  sqrt = find_square_root(num)
  return sqrt * sqrt == num

# square_tests = [4,16,21,25,48,49,50,55,81,101]
# print("Squares:")
# for test in square_tests:
#   print(test, isSquare(test))

# prime_tests = [*list(range(2, 12)), 25, 31, 32, 44, 57, 59, 91, 93, 97]
# print("\nPrimes:")
# for test in prime_tests:
#   print(test, isPrime(test))

for i in range(100, 100001):
  output = "FooBar"
  if isPrime(i):
    output = "Foo"
  elif isSquare(i):
    output = "Bar"
  print(f"{i}: {output}")