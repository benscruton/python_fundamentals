def make_change(amount):
    coin_values = {
        "hundred_dollar_bill": 10000,
        "fifty_dollar_bill": 5000,
        "twenty_dollar_bill": 2000,
        "ten_dollar_bill": 1000,
        "five_dollar_bill": 500,
        "one_dollar_bill": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1,
    }

    output = {}
    for k in coin_values:
        num_of_these = 0
        while amount >= coin_values[k]:
            amount -= coin_values[k]
            num_of_these += 1
        output[k] = num_of_these
    return output

def sep(how_long = 20):
    print("*" * how_long)

def print_dict_nice(d):
    longest = max([len(k) for k in d]) + 1
    for k in d:
        display_k = k + ":" + (" " * (longest - len(k)))
        print(f"{display_k} {d[k]}")







print_dict_nice(make_change(100)) # one dollar bill
sep(30)
print_dict_nice(make_change(67))  # two quarters, one dime, one nickel, two pennies
sep(30)
print_dict_nice(make_change(813274124))