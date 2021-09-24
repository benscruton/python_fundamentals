def print_iter(it):
    while True:
        try:
            print(next(it))
        except:
            break



x = [False, False, 0, None, "", {}]
y = [False, [], 1, True]
z = [2, True, "hello"]

# print(all(x))   # False
# print(any(x))   # False

# print(all(y))   # False
# print(any(y))   # True

# print(all(z))   # True
# print(any(z))   # True

# it = iter(y)
# print(all(it))  # False
# print(next(it)) # False
# print(next(it)) # ""
# print(all(it))  # True?

# it = iter(y)
# print(all(it))
# print(all(it))
# print(all(it))
# print(all(it))

a = {
    "hello": True,
    "goodbye": False,
    "word": "yes"
}

it = iter({**a})
# print_iter(it)

b = {**a}
c = a

b["hello"] = False
print(a)
c["hello"] = None
print(a)

def subtract(x, y):
    diff = x - y
    print(diff)
    return diff

nums = {
    "y": 2,
    "x": 1
}

subtract(**nums)