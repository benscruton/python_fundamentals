def compare(list_one, list_two):
  if len(list_one) != len(list_two):
    return print("The lists are not the same.")
  for i in range(len(list_one)):
    if list_one[i] != list_two[i]:
      return print("The lists are not the same.")
  return print("The lists are the same.")

list_one = [1,2,5,6,2]
list_two = [1,2,5,7,2]
compare(list_one, list_two) #same

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare(list_one, list_two) #not same

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare(list_one, list_two) #not same

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare(list_one, list_two) #not same