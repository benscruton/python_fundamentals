def nums_forever():
    i = 0
    while True:
        i += 1
        yield i

def try_next(it):
    try:
        print(next(it))
    except StopIteration:
        print("The stream ended.")
    except:
        print("Something else went wrong.")



try_next(nums_forever()) # 1
try_next(nums_forever()) # 1

it = nums_forever()
try_next(it) # 1
try_next(it) # 2
try_next(it) # 3
try_next(it) # 4
it.send("hello") # returns 5 but does not print anything
try_next(it) # 6
it.close() 
try_next(it) # "The stream ended."

def count(max):
    i = 0
    while i < max:
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += 1

it = count(10)
try_next(it)
try_next(it)
print(it.send(6))
try_next(it)
try_next(it)
it.send(-3)
try_next(it)
try_next(it)
try_next(it)
try_next(it)