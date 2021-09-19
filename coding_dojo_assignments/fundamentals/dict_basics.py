person1 = {
  "name": "Anna",
  "age": 23,
  "country of birth": "United States",
  "favorite language": "Python"
}

person2 = {
  "name": "Mordeth",
  "age": "unknown",
  "favorite thing": "more death"
}

def print_dict(d):
  for k, v in d.items():
    print(f"My {k} is {v}.")

print_dict(person1)
print_dict(person2)