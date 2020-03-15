from collections import deque

def roll(dice, dice_num, board, direction, floor, location) :
    if location[0] == 0 and direction == 3 : 
        return dice, dice_num, board, floor, location
    if location[0] == len(board) - 1 and direction == 4 :
        return dice, dice_num, board, floor, location
    if location[1] == 0 and direction == 2 :
        return dice, dice_num, board, floor, location
    if location[1] == len(board[0]) - 1 and direction == 1 :
        return dice, dice_num, board, floor, location
    vector = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    if direction == 1 :
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif direction == 2 :
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif direction == 3 :
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    else :
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    
    floor = dice[1][1]
    ceiling = 7 - floor
    location[0] += vector[direction - 1][0]
    location[1] += vector[direction - 1][1]
    board, dice_num = change(dice_num, floor, board, location)

    print(dice_num[ceiling - 1])
    return dice, dice_num, board, floor, location

def change(dice_num, floor, board, location) :
    x, y = location[0], location[1]
    if board[x][y] == 0 :
        board[x][y] = dice_num[floor - 1]
    else :
        dice_num[floor - 1] = board[x][y]
        board[x][y] = 0

    return board, dice_num

if __name__ == "__main__" :
    start = list(map(int, input().split(" ")))
    N, M, x, y, K = start[0], start[1], start[2], start[3], start[4]
    board = []
    dice_num = [0, 0, 0, 0, 0, 0]
    dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
    floor = dice[1][1]

    for i in range(N) :
        num = list(map(int, input().split(" ")))
        board.append(num)
    
    move = list(map(int, input().split(" ")))
    move = deque(move)

    location = [x, y]
    num = 0
    while move :
        direction = move.popleft()
        dice, dice_num, board, floor, location = roll(dice, dice_num, board, direction, floor, location)
        num += 1

###correct###