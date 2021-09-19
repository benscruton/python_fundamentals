def create_multiplication_table(max = 12, min = 1):
  if(max < min):
    return print("Max cannot be smaller than min.")
  length = 2
  length_helper = max ** 2
  while(length_helper):
    length += 1
    length_helper //= 10

  top_row = ["x │", *list(range(min, max + 1))]
  second_row = ["─" * (length - 1) + "┼"]
  for i in range(max - min + 1):
    second_row.append("─" * length)
  table = [top_row, second_row]

  for i in range(min, max + 1):
    row = [f"{i} │"]
    for j in range(min, max + 1):
      row.append(i * j)
    table.append(row)

  output = ""
  for row in table:
    line = ""
    for val in row:
      val = str(val)
      line += " "*(length - len(val)) + val
    output += line + "\n"
  print(output)

create_multiplication_table(1002, 993)