words = "it's thanksgiving day.  it's my birthday, too!"

print(words.find("day"))
words = words.replace("day", "month")
print(words)


x = [2,54,-2,7,12,98]
print(min(x))
print(max(x))
x.sort()
print(x)


y = ["hello",2,54,-2,7,12,98,"world"]
print(y[0], y[-1])



z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
z = [z[:len(z) // 2], *[val for val in z[len(z) // 2:]]]
print(z)