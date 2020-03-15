from collections import deque
import copy

def tetromino(board) :
    answer = []
    for idx_i, i in enumerate(board) :
        for idx_j, j in enumerate(i) :
            temp = []
            a = total(board, idx_i, idx_j)
            b = fuck(board, idx_i, idx_j, a)
            for k in b :
                plus = 0
                for l in k :
                    plus += board[l[0]][l[1]]
                temp.append(plus)
            answer.append(max(temp))
    print(max(answer))

def total(board, x, y) :
    N = len(board)
    M = len(board[0])
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    q = deque()
    q.append([(x, y)])
    flag = True
    while flag :
        start = q.popleft()
        if len(start) == 4 :
            q.append(start)
            break
        last = start.pop()
        for i in range(4) :
            x, y = last[0], last[1]
            tmp = copy.deepcopy(start)
            tmp.append((x, y))
            x += direction[i][0]
            y += direction[i][1]
            if x >= 0 and x < N and y >= 0 and y < M :
                if (x, y) not in tmp :
                    tmp.append((x, y))
                    q.append(tmp)
    return q

def fuck(board, x, y, q) :
    N = len(board)
    M = len(board[0])
    if x >= 0 and x + 1 < N and y >= 0 and y + 2 < M :
        q.append([(x, y), (x, y + 1), (x, y + 2), (x + 1, y + 1)])
    if x < N and x - 1 >= 0 and y >= 0 and y + 2 < M :
        q.append([(x, y), (x, y + 1), (x, y + 2), (x - 1, y + 1)])
    if x >= 0 and x + 2 < N and y >= 0 and y + 1 < M :
        q.append([(x, y), (x + 1, y), (x + 1, y + 1), (x + 2, y)])
    if x >= 0 and x + 2 < N and y + 1 < M and y - 1 >= 0 :
        q.append([(x, y), (x + 1, y), (x + 2, y), (x + 1, y + 1)])

    return q

if __name__ == "__main__" :
    N, M = input().split(" ")
    N = int(N)
    M = int(M)
    board = []

    for i in range(N) :
        num = list(map(int, input().split(" ")))
        board.append(num)
    tetromino(board)