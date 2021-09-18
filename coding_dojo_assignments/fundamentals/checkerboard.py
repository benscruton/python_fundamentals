def checkerboard(height = 8, length = 8):
  board = []
  for i in range(height):
    row = ""
    for j in range(length):
      row += "░░" if (i + j) % 2 else "▓▓"
    board.append(row)
  for row in board:
    print(row)


def line_break():
  print()
  print("----------")
  print()

checkerboard()
line_break()
checkerboard(4, 4)
line_break()
checkerboard(20)
line_break()
checkerboard(length = 20)