from collections import deque
import copy

def move(direction, board, answer) :
    board2 = copy.deepcopy(board)
    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == "R" : 
                R_x, R_y = idx_i, idx_j

    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == "B" : 
                B_x, B_y = idx_i, idx_j

    if direction == 0 :
        temp_R = R_x - 1
        temp_B = B_x - 1
        ret = relation(direction, (R_x, R_y), (B_x, B_y))
        if ret == 0 :
            while True :
                if board[temp_B][B_y] == 'O' :
                    return 0
                elif board[temp_B][B_y] != '.' :
                    board2[B_x][B_y], board2[temp_B + 1][B_y] = board2[temp_B + 1][B_y], board2[B_x][B_y]
                    break
                else :
                    temp_B -= 1
            while True :
                if board[temp_R][R_y] == 'O' :
                    print(answer)
                    exit()
                elif board[temp_R][R_y] != '.' :
                    board2[R_x][R_y], board2[temp_R + 1][R_y] = board2[temp_R + 1][R_y], board2[R_x][R_y]
                    break
                else :
                    temp_R -= 1
        elif ret == 1 :
            while True :
                if board[temp_R][R_y] == 'O' :
                    print(answer)
                    exit()
                elif board[temp_R][R_y] != '.' :
                    board2[R_x][R_y], board2[temp_R + 1][R_y] = board2[temp_R + 1][R_y], board2[R_x][R_y]
                    board2[B_x][B_y], board2[temp_R + 2][B_y] = board2[temp_R + 2][B_y], board2[B_x][B_y]
                    break
                else :
                    temp_R -= 1
        elif ret == 2 :
            while True :
                if board[temp_B][B_y] == 'O' :
                    return 0
                elif board[temp_R][R_y] != '.' :
                    board2[B_x][B_y], board2[temp_B + 1][B_y] = board2[temp_B + 1][B_y], board2[B_x][B_y]
                    board2[R_x][R_y], board2[temp_B + 2][R_y] = board2[temp_B + 2][R_y], board2[R_x][R_y]
                    break
                else :
                    temp_B -= 1
        
    elif direction == 1 :
        temp_R = R_y + 1
        temp_B = B_y + 1
        ret = relation(direction, (R_x, R_y), (B_x, B_y))
        if ret == 0 :
            while True :
                if board[B_x][temp_B] == 'O' :
                    return 0
                elif board[B_x][temp_B] != '.' :
                    board2[B_x][B_y], board2[B_x][temp_B - 1] = board2[B_x][temp_B - 1], board2[B_x][B_y]
                    break
                else :
                    temp_B += 1
            while True :
                if board[R_x][temp_R] == 'O' :
                    print(answer)
                    exit()
                elif board[R_x][temp_R] != '.' :
                    board2[R_x][R_y], board2[R_x][temp_R - 1] = board2[R_x][temp_R - 1], board2[R_x][R_y]
                    break
                else :
                    temp_R += 1
        elif ret == 1 :
            while True :
                if board[R_x][temp_R] == 'O' :
                    print(answer)
                    exit()
                elif board[R_x][temp_R] != '.' :
                    board2[R_x][R_y], board2[R_x][temp_R - 1] = board2[R_x][temp_R - 1], board2[R_x][R_y]
                    board2[B_x][B_y], board2[B_x][temp_R - 2] = board2[B_x][temp_R - 2], board2[B_x][B_y]
                    break
                else :
                    temp_R += 1
        elif ret == 2 :
            while True :
                if board[B_x][temp_B] == 'O' :
                    return 0
                elif board[B_x][temp_B] != '.' :
                    board2[B_x][B_y], board2[B_x][temp_B - 1] = board2[B_x][temp_B - 1], board2[B_x][B_y]
                    board2[R_x][R_y], board2[R_x][temp_B - 2] = board2[R_x][temp_B - 2], board2[R_x][R_y]
                    break
                else :
                    temp_B += 1

    elif direction == 2 :
        temp_R = R_x + 1
        temp_B = B_x + 1
        ret = relation(direction, (R_x, R_y), (B_x, B_y))
        if ret == 0 :
            while True :
                if board[temp_B][B_y] == 'O' :
                    return 0
                elif board[temp_B][B_y] != '.' :
                    board2[B_x][B_y], board2[temp_B - 1][B_y] = board2[temp_B - 1][B_y], board2[B_x][B_y]
                    break
                else :
                    temp_B += 1
            while True :
                if board[temp_R][R_y] == 'O' :
                    print(answer)
                    exit()
                elif board[temp_R][R_y] != '.' :
                    board2[R_x][R_y], board2[temp_R - 1][R_y] = board2[temp_R - 1][R_y], board2[R_x][R_y]
                    break
                else :
                    temp_R += 1
        elif ret == 1 :
            while True :
                if board[temp_R][R_y] == 'O' :
                    print(answer)
                    exit()
                elif board[temp_R][R_y] != '.' :
                    board2[R_x][R_y], board2[temp_R - 1][R_y] = board2[temp_R - 1][R_y], board2[R_x][R_y]
                    board2[B_x][B_y], board2[temp_R - 2][B_y] = board2[temp_R - 2][B_y], board2[B_x][B_y]
                    break
                else :
                    temp_R += 1
        elif ret == 2 :
            while True :
                print(temp_B, B_y)
                if board[temp_B][B_y] == 'O' :
                    return 0
                elif board[temp_R][R_y] != '.' :
                    board2[B_x][B_y], board2[temp_B - 1][B_y] = board2[temp_B - 1][B_y], board2[B_x][B_y]
                    board2[R_x][R_y], board2[temp_B - 2][R_y] = board2[temp_B - 2][R_y], board2[R_x][R_y]
                    break
                else :
                    temp_B += 1

    elif direction == 3 :
        temp_R = R_y - 1
        temp_B = B_y - 1
        ret = relation(direction, (R_x, R_y), (B_x, B_y))
        if ret == 0 :
            while True :
                if board[B_x][temp_B] == 'O' :
                    return 0
                elif board[B_x][temp_B] != '.' :
                    board2[B_x][B_y], board2[B_x][temp_B + 1] = board2[B_x][temp_B + 1], board2[B_x][B_y]
                    break
                else :
                    temp_B -= 1
            while True :
                if board[R_x][temp_R] == 'O' :
                    print(answer)
                    exit()
                elif board[R_x][temp_R] != '.' :
                    board2[R_x][R_y], board2[R_x][temp_R + 1] = board2[R_x][temp_R + 1], board2[R_x][R_y]
                    break
                else :
                    temp_R -= 1
        elif ret == 1 :
            while True :
                if board[R_x][temp_R] == 'O' :
                    print(answer)
                    exit()
                elif board[R_x][temp_R] != '.' :
                    board2[R_x][R_y], board2[R_x][temp_R + 1] = board2[R_x][temp_R + 1], board2[R_x][R_y]
                    board2[B_x][B_y], board2[B_x][temp_R + 2] = board2[B_x][temp_R + 2], board2[B_x][B_y]
                    break
                else :
                    temp_R -= 1
        elif ret == 2 :
            while True :
                if board[B_x][temp_B] == 'O' :
                    return 0
                elif board[B_x][temp_B] != '.' :
                    board2[B_x][B_y], board2[B_x][temp_B + 1] = board2[B_x][temp_B + 1], board2[B_x][B_y]
                    board2[R_x][R_y], board2[R_x][temp_B + 2] = board2[R_x][temp_B + 2], board2[R_x][R_y]
                    break
                else :
                    temp_B -= 1
    return board2

def relation(direction, R, B) :
    R_x, R_y, B_x, B_y = R[0], R[1], B[0], B[1]
    if R_x != B_x and R_y != B_y :
        return 0
    elif direction == 0 :
        if R_y != B_y :
            return 0
        elif R_x < B_x :
            return 1
        else :
            return 2
    elif direction == 1 :
        if R_x != B_x :
            return 0
        elif R_y > B_y :
            return 1
        else :
            return 2
    elif direction == 2 :
        if R_y != B_y :
            return 0 
        elif R_x > B_x :
            return 1
        else :
            return 2
    else :
        if R_x != B_x :
            return 0
        elif R_y < B_y :
            return 1 
        else :
            return 2

if __name__ == "__main__" :
    N, M = input().split(" ")
    print(M)
    N = int(N)
    M = int(M)
    board = []
    q1 = deque()
    answer = 1
    print(N)
    for i in range(N) :
        string = list(input())
        board.append(string)
        print(i)
    for i in board :
        print(board)
    q1.append(board)
    
    while answer <= 10 :
        q2 = deque()
        while q1 :
            temp1 = q1.popleft()
            for i in range(4) :
                for j in temp1 :
                    print(j)
                temp2 = move(i, temp1, answer)
                if temp2 != 0 :
                    q2.append(temp2)
        answer += 1
        q1 = copy.copy(q2)
    print(-1)