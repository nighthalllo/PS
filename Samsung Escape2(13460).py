from collections import deque
import copy

def move(board, answer, di, dj) :
    temp = copy.deepcopy(board)
    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == "R" : 
                R_x, R_y = idx_i, idx_j

    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == "B" : 
                B_x, B_y = idx_i, idx_j

    temp_R = [R_x + di, R_y + dj]
    temp_B = [B_x + di, B_y + dj]

    while True :
        if board[temp_R[0]][temp_R[1]] == '.' or board[temp_R[0]][temp_R[1]] == 'B':
            temp_R[0] += di
            temp_R[1] += dj
        else :
            break
    while True :
        if board[temp_B[0]][temp_B[1]] == '.' or board[temp_B[0]][temp_B[1]] == 'R':
            temp_B[0] += di
            temp_B[1] += dj
        else :
            break
    if temp_R == temp_B :
        if board[temp_R[0]][temp_R[1]] == 'O' :
            return 0
        else :
            if (R_x - B_x) * di > 0 or (R_y - B_y) * dj:
                temp[R_x][R_y], temp[temp_R[0] - di][temp_R[1] - dj] = temp[temp_R[0] - di][temp_R[1] - dj], temp[R_x][R_y]
                temp[B_x][B_y], temp[temp_B[0] - (di * 2)][temp_B[1] - (dj * 2)] = temp[temp_B[0] - (di * 2)][temp_B[1] - (dj * 2)], temp[B_x][B_y]
            else :
                temp[R_x][R_y], temp[temp_R[0] - (di * 2)][temp_R[1] - (dj * 2)] = temp[temp_R[0] - (di * 2)][temp_R[1] - (dj * 2)], temp[R_x][R_y]
                temp[B_x][B_y], temp[temp_B[0] - di][temp_B[1] - dj] = temp[temp_B[0] - di][temp_B[1] - dj], temp[B_x][B_y]
    else :
        if board[temp_R[0]][temp_R[1]] == 'O' :
            print(answer)
            exit()
        else :
            temp[R_x][R_y], temp[temp_R[0] - di][temp_R[1] - dj] = temp[temp_R[0] - di][temp_R[1] - dj], temp[R_x][R_y]
            temp[B_x][B_y], temp[temp_B[0] - di][temp_B[1] - dj] = temp[temp_B[0] - di][temp_B[1] - dj], temp[B_x][B_y]

    return temp

if __name__ == "__main__" :
    N, M = input().split(" ")
    N = int(N)
    M = int(M)
    board = []
    q1 = deque()
    answer = 1

    for i in range(N) :
        string = list(input())
        board.append(string)
    q1.append(board)
    
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while answer <= 8 :
        q2 = deque()
        while q1 :
            temp1 = q1.popleft()
            for i in range(4) :
                temp2 = move(temp1, answer, direction[i][0], direction[i][1])
                if temp2 != 0 :
                    q2.append(temp2)
        print(answer)
        answer += 1
        q1 = copy.deepcopy(q2)
    print(-1)