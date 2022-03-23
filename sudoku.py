board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# this function print the board on the terminal
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:
            print('- - - - - - - - - - ')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# this function checks for empty spots will return the (x, y) of the spot
def check_empty_spot(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def validate_spot(spot, num, bo):
    """
    we put a number in the board then we see if it is a valid number or not
    """
    # check row
    for i in range(len(bo[0])):
        if bo[spot[0]][i] == num and i != spot[1]:
            return False
       
    # check column
    for j in range(len(bo)):
        if bo[j][spot[1]] == num and j != spot[0]:
            return False
    # check box
    box_x = spot[1] // 3
    box_y = spot[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != spot:
                return False
    return True


def solve(bo):
    """ we check if there is an empty spot, if not we assume that the board is complete
    then, if there is one we take it and try number on it to see if its a valid number, if yes we put it on the board
    and see if the board is complete or not with recursion if no we try another number"""
    empty_spot = check_empty_spot(bo)
    if not empty_spot:
        return True
    else:
        spot_y, spot_x = empty_spot
    for i in range(1, 10):
        if validate_spot((spot_y, spot_x), i, bo):
            bo[spot_y][spot_x] = i
            if solve(bo):
                return True
            bo[spot_y][spot_x] = 0
    
    return False
        
print_board(board)
solve(board)
print(" ")
print_board(board)