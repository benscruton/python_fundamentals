def make_dict(list1, list2):
    new_dict = {}
    inverted = len(list2) > len(list1)
    keys = list2 if inverted else list1
    values = list1 if inverted else list2
    for i in range(len(values)):
        new_dict[keys[i]] = values[i]
    return new_dict

name_eq = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal_eq = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


name_longer = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oksana", "Oscar"]
favorite_animal_shorter = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "sable"]


d1 = make_dict(name_eq, favorite_animal_eq)
d2 = make_dict(name_longer, favorite_animal_shorter)
d3 = make_dict(favorite_animal_shorter, name_longer)

print(d1)
print(d2)
print(d3)