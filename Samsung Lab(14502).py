import copy
from itertools import combinations

def virus(board) :
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while True :
        cnt = 0
        for idx_i, i in enumerate(board) :
            for idx_j, j in enumerate(i) :
                if j == 2 :
                    for k in range(4) :
                        if board[idx_i + direction[k][0]][idx_j + direction[k][1]] == 0 :
                            board[idx_i + direction[k][0]][idx_j + direction[k][1]] = 2
                            cnt += 1
        if cnt == 0 :
            return board

if __name__ == "__main__" :
    start = time.time()
    N, M = input().split(" ")
    N, M = int(N), int(M)

    board = []
    board.append([1] * (M + 2))
    idx = []

    answer = 0

    for i in range(N) :
        
        string = "1" + input().replace(" ", "") + "1"
        string = [int(i) for i in string]
        board.append(string)
    
    board.append([1] * (M + 2))
    
    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            if j == 0 :
                idx.append((idx_i, idx_j))
    
    combi = list(combinations(idx, 3))

    original = copy.deepcopy(board)

    for i in combi :
        result = 0
        for j in i :
            board[j[0]][j[1]] = 1
        for i in virus(board) :   
            result += i.count(0)
        if result > answer :
            answer = result
        board = copy.deepcopy(original)
    print(answer)