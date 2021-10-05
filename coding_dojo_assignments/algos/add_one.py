# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def add_one_orig(digits):
    place = len(digits) - 1
    digits[place] += 1
    while digits[place] == 10 and place > 0:
        digits[place] = 0
        place -= 1
        digits[place] += 1
    if digits[0] == 10:
        digits[0] = 0
        digits.insert(0, 1)
    return digits

def add_one(digits):
    i = len(digits) - 1
    go = True
    while go and i >= 0:
        digits[i] = (digits[i] + 1) % 10
        go = not digits[i]
    if go:
        digits.insert(0, 1)
    return digits
