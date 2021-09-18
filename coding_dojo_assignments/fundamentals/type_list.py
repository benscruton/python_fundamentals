# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"



def type_list(l):
  if len(l) == 0:
    return print("There are no items in the list")
  list_type = str(type(l[0]))
  total = 0
  full_string = ""
  show = {
    "total": False,
    "full_string": False
  }

  for item in l:
    if str(type(item)) != list_type:
      list_type = "mixed"
    if type(item) == int or type(item) == float:
      total += item
      show["total"] = True
    elif type(item) == str:
      full_string += " " if len(full_string) else ""
      full_string += item
      show["full_string"] = True

  if list_type == str(int):
    list_type = "integer"
  elif list_type == str(float):
    list_type = "floating point number"
  elif list_type == str(str):
    list_type = "string"
  print(f"The list you entered is of {list_type} type.")
  if show["full_string"]:
    print(f"String: {full_string}")
  if show["total"]:
    print(f"Sum: {total}")
  print()

print()

type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])