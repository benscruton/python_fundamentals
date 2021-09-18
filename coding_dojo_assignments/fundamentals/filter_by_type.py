def filter_by_type(input):
  if type(input) == int:
    print("That's a big number" if input >= 100 else "That's a small number")
  elif type(input) == str:
    print("Long sentence" if len(input) >= 50 else "Short sentence")
  elif type(input) == list:
    print("Big list!" if len(input) >= 10 else "Short list.")
  else:
    print("Input type not recognized.")

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

tests = [ sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

for test in tests:
  filter_by_type(test)