from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
q = deque()

def get(i, j) :
    if board[i][j] :
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj) :
    while q :
        x = q.popleft()
        if not board[i][j] :
            board[i][j] = x
        elif board[i][j] == x :
            board[i][j] = x*2
            i,j  = i + di, j + dj
        else :
            i,j  = i + di, j + dj
            board[i][j] = x

def move(k) :
    if k == 0 :
        for j in range(n) :
            for i in range(n) :
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1 :
        for j in range(n) :
            for i in range(n-1, -1, -1) :
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2 :
        for i in range(n) :
            for j in range(n) :
                get(i, j)
            merge(i, 0, 0, 1)
    else :
        for i in range(n) :
            for j in range(n-1, -1, -1) :
                get(i, j)
            merge(i, n-1, 0, -1)

def dfs(cnt) :
    global board, answer
    if cnt == 5 :
        for i in range(n) :
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4) :
        move(k)
        dfs(cnt+1)
        board = [x[:] for x in b]

dfs(0)
print(answer)