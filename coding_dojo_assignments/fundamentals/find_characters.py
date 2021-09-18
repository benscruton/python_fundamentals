# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

def find_character(l, char):
  if len(char) != 1:
    return print("Please only enter one character.")
  output = [item for item in l if char in item]
  print(output)
  return output

find_character(['hello','world','my','name','is','Anna'], "o")