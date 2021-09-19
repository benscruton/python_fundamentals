def draw_stars(l):
  for item in l:
    if type(item) == int:
      print("*" * item)
    elif type(item) == str:
      print(item[0].lower() * len(item))

draw_stars([4, "Tom", 1, "Michael", 5, [], 7, "Jimmy Smith"])