class Mathematics:
    def __init__(self):
        self.value = 0

    def add(self, *nums):
        l = self.flatten_list(nums)
        l = self.remove_non_numbers(l)
        for num in l:
            self.value += num
        return self
    
    def subtract(self, *nums):
        l = self.flatten_list(nums)
        l = self.remove_non_numbers(l)
        for num in l:
            self.value -= num
        return self

    def result(self):
        print(f"Value: {self.value}")
        return self.value

    def clear(self):
        self.value = 0
        return self

    def flatten_list(self, l):
        l = list(l)
        i = 0
        while i < len(l):
            if type(l[i]) == list or type(l[i]) == tuple:
                new_items = self.flatten_list(l[i])
                l[i:i+1] = new_items
            else:
                i += 1
        return l
    
    def remove_non_numbers(self, l):
        l = list(l)
        i = 0
        while i < len(l):
            if type(l[i]) == int or type(l[i]) == float:
                i += 1
            else:
                l.pop(i)
        return l
    

    
m = Mathematics()
# print(type(m))

# l = 1, 2, "hello",[3,"blarg",[6, 7, [8,9,10], 11.5], 4], 5
# print("Original:\n",l)
# l = m.flatten_list(l)
# print("Flattened:\n", l)
# l = m.remove_non_numbers(l)
# print("Only numbers:\n", l)

m.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result() # 28.15

m.clear().result() # 0

m.add([1, 2], (5, 6, [7,8,(9, 10)])).result() # 48
m.subtract(2, (4, 5), [1]).result() # 36