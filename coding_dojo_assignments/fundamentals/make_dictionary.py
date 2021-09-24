def make_dict_orig(list1, list2):
    new_dict = {}
    inverted = len(list2) > len(list1)
    keys = list2 if inverted else list1
    values = list1 if inverted else list2
    for i in range(len(values)):
        new_dict[keys[i]] = values[i]
    return new_dict

def make_dict(list1, list2):
    zipped = zip(list2, list1) if len(list2) > len(list1) else zip(list1, list2)
    return dict(zipped)
    


name_eq = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal_eq = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


name_longer = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oksana", "Oscar"]
favorite_animal_shorter = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "sable"]


d1 = make_dict(name_eq, favorite_animal_eq)
d2 = make_dict(name_longer, favorite_animal_shorter)
d3 = make_dict(favorite_animal_shorter, name_longer)

print(d1)
print("*"*30)
print(d2)
print("*"*30)
print(d3)