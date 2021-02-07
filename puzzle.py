import doctest
def check_rows(board):
    """
    This function returns True if rows consists only of free spaces,
    white spaces and number 1-9.
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_rows(["**** ****", "1**1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for row in board:
        for element in row:
            if element != ' ' and element != '*':
                if int(element) < 1 or int(element) > 9:
                    return False
                if row.count(element) > 1:
                    return False
                if len(row) != 9:
                    return False
    return True
# print(check_rows(["**** ****", "1**1 ****", "**  3****", "* 4  ****", "     9 5 ",
#                  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))

def columns(board):
    """
    This function returns list of columns on the board.
    >>> columns(["**** ****", "***1 ****", "**  3****",\
     "* 4  ****", "     9 5 ", " 6  83  *", "3   1  **",\
     "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82',\
 '*1       ', '  3  81  ', '****93 2*',\
 '****   **', '****5 ***', '**** ****']
    """
    new_board = []
    for i in range(0, len(board)):
        new_row = ''
        for row in board:
            new_row += row[i]
        new_board.append(new_row)
    return new_board
# print(columns(["**** ****", "***1 ****", "**  3****", "* 4  ****", "     9 5 ",
#                  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))

def check_columns(board):
    """
    This function returns True if columns consists only of free spaces,
    white spaces and number 1-9.
    >>> check_columns(["**** ****", "***1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_columns(["**** ****", "3**1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    return(check_rows(columns(board)))
# print(check_columns(["**** ****", "3**1 ****", "**  3****", "* 4  ****",\
    # "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))

def create_color_blocks(board):
    """
    This function creates list of spaces\
    painted in one color on the board.
    >>> create_color_blocks(["**** ****", "***1 ****",\
     "**  3****", "* 4  ****", "     9 5 ", " 6  83  *",\
     "3   1  **", "  8  2***", "  2  ****"])
    [' 2  ********  3  ', '8  2******  6  ', ' 1  **** 4   ',\
 '83  **1    ', '9 5   3  ', '*******', '*****', '***']
    """
    blocks = []
    rows = board
    columns_list = columns(board)
    num = 0
    for i in range(8, 0, -1):
        blocks.append(rows[i][num + 1:] + columns_list[num][:(9 - num)])
        num += 1
    return blocks
# print(create_color_blocks(["**** ****", "***1 ****", "**  3****", "* 4  ****", "     9 5 ",
                #  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))

def check_color_blocks(board):
    """
    This function returns True if columns consists only of free spaces,
    white spaces and number 1-9.
    >>> check_columns(["**** ****", "***1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_columns(["**** ****", "3**1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    board = create_color_blocks(board)
    for row in board:
        for element in row:
            if element != ' ' and element != '*':
                if row.count(element) > 1:
                    return False
    return True
# print(check_color_blocks(["**** ****", "***1 ****", "**  3****", "* 4  ****", "     9 5 ",
#                  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]))


def validate_board(board):
    """
    This function checks whether board is correct.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4  ****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    if check_rows(board) is False:
        return False
    if check_columns(board) is False:
        return False
    if check_color_blocks(board) is False:
        return False
    return True


if __name__ == "__main__":
    print(validate_board(["6*** ****", "***1 ****",
                          "**  3****", "* 4 7****",
                          "     9 5 ", " 6  83  *",
                          "3   1  **", "  8  2***",
                          "  2  *6**"]))
doctest.testmod()