def get_horiz_separator(position):
    first = {
        "top": "┌",
        "middle": "├",
        "bottom": "└"
    }
    center = {
        "top": "┬",
        "middle": "┼",
        "bottom": "┴"
    }
    last = {
        "top": "┐",
        "middle": "┤",
        "bottom": "┘"
    }
    horiz_separator = first[position]
    horiz_separator += "─" * 7 + center[position]
    horiz_separator += "─" * 7 + center[position]
    horiz_separator += "─" * 7 + last[position]
    return horiz_separator

def print_board(board):
    print("\n" + get_horiz_separator("top"))
    for i in range(9):
        row = "│"
        for j in range(9):
            row += " " + board[i][j]
            if j % 3 == 2 and j < 8:
                row += " │"
        row += " │"
        print(row)
        if i % 3 == 2 and i < 8:
            print(get_horiz_separator("middle"))
    print(get_horiz_separator("bottom") + "\n")

def check_board_at_spot(board, i, j):
    here = board[i][j]
    if here == ".":
        return True

    # check vertical row:
    for k in range(9):
        if k == i:
            continue
        if board[k][j] == here:
            return False
        
    # check horizontal row:
    for k in range(9):
        if k == j:
            continue
        if board[i][k] == here:
            return False
    
    # check each 3x3 box:
    for k in range(9):
        i_start = i - (i % 3)
        j_start = j - (j % 3)
        skip = (i // 3) + (j % 3)

        square_val = board[i_start + (k // 3)][j_start + (k % 3)]
        if square_val == "." or k == skip:
            continue
        if square_val == here:
            return False
    
    return True


def get_horiz_separator(position):

    first = {
        "top": "┌",
        "middle": "├",
        "bottom": "└"
    }
    center = {
        "top": "┬",
        "middle": "┼",
        "bottom": "┴"
    }
    last = {
        "top": "┐",
        "middle": "┤",
        "bottom": "┘"
    }

    horiz_separator = first[position]
    horiz_separator += "─" * 7 + center[position]
    horiz_separator += "─" * 7 + center[position]
    horiz_separator += "─" * 7 + last[position]
    return horiz_separator



def advance_iterators(i, j):
    j += 1
    if j == 9:
        i += 1
        j = 0
    return i, j







def make_progress(board):
    possible = [True] * 9
    possible.insert(0, "placeholder")

    progress_made = True

    while progress_made:
        progress_made = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    possible_here = [*possible]
                    for k in range(9):
                        # check row:
                        if board[i][k] != ".":
                            possible_here[int(board[i][k])] = False
                        # check column:
                        if board[k][j] != ".":
                            possible_here[int(board[k][j])] = False
                        # check square
                        


def backtrack(board, i = 0, j = 0):
    print(f"i: {i}    j: {j}")
    while i < 9 and board[i][j] != ".":
        i, j = advance_iterators(i, j)
    if i >= 9:
        return True
    
    possible_nums = []
    for k in range(1, 10):
        board[i][j] = str(k)
        if check_board_at_spot(board, i, j):
            possible_nums.append(str(k))
    board[i][j] = "."

    if not len(possible_nums):
        return False
    
    for num in possible_nums:
        print(num)
        board[i][j] = num
        test_i, test_j = advance_iterators(i, j)
        if backtrack(board, test_i, test_j):
            return True
    board[i][j] = "."
    










test_case = [
    [ "5", "3", ".",   ".", "7", ".",   ".", ".", "." ],

    [ "6", ".", ".",   "1", "9", "5",   ".", ".", "." ],

    [ ".", "9", "8",   ".", ".", ".",   ".", "6", "." ],


    [ "8", ".", ".",   ".", "6", ".",   ".", ".", "3" ],

    [ "4", ".", ".",   "8", ".", "3",   ".", ".", "1" ],

    [ "7", ".", ".",   ".", "2", ".",   ".", ".", "6" ],


    [ ".", "6", ".",   ".", ".", ".",   "2", "8", "." ],

    [ ".", ".", ".",   "4", "1", "9",   ".", ".", "5" ],

    [ ".", ".", ".",   ".", "8", ".",   ".", "7", "9" ]
]

# print_board(test_case)

# print(backtrack(test_case))

print_board(test_case)

for i in range(1, 10):
    test_case[0][2] = str(i)
    print(i, check_board_at_spot(test_case, 0, 2))