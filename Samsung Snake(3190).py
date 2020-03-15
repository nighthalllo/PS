from collections import deque

if __name__ == "__main__" :

    snake = deque()
    go = deque()

    head = (0, 0)
    
    answer = 0

    N = int(input())
    K = int(input())

    board = [[0] * N for i in range(N)]
    
    for i in range(K) :
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        board[x - 1][y - 1] = 1
    
    L = int(input())
    
    for i in range(L) :
        X, C = input().split(" ")
        X = int(X)
        go.append((X, C))

    direct = 1
    snake.append(head)
    while go :
        direction = go.popleft()
        X = direction[0]
        C = direction[1]
        if direct == 0 :
            while answer < X :
                answer += 1
                head = snake[-1]
                x, y = head[0], head[1]
                x -= 1
                if x < 0 or (x, y) in snake :
                    print(answer)
                    exit()
                snake.append((x, y))
                if board[x][y] == 1 :
                    board[x][y] = 0
                else :
                    snake.popleft()
        elif direct == 1 :
            while answer < X :
                answer += 1
                head = snake[-1]
                x, y = head[0], head[1]
                y += 1
                if y >= N or (x, y) in snake :
                    print(answer)
                    exit()
                snake.append((x, y))
                if board[x][y] == 1 :
                    board[x][y] = 0
                else :
                    snake.popleft()
        elif direct == 2 :
            while answer < X :
                answer += 1
                head = snake[-1]
                x, y = head[0], head[1]
                x += 1
                if x >= N or (x, y) in snake :
                    print(answer)
                    exit()
                snake.append((x, y))
                if board[x][y] == 1 :
                    board[x][y] = 0
                else :
                    snake.popleft()
        else :
            while answer < X :
                answer += 1
                head = snake[-1]
                x, y = head[0], head[1]
                y -= 1
                if y < 0 or (x, y) in snake :
                    print(answer)
                    exit()
                snake.append((x, y))
                if board[x][y] == 1 :
                    board[x][y] = 0
                else :
                    snake.popleft()
        if C == 'D' :
            direct = (direct + 1) % 4
        else :
            direct = (direct - 1) % 4
    
    if direct == 0 :
        while True :
            answer += 1
            head = snake[-1]
            x, y = head[0], head[1]
            x -= 1
            if x < 0 or (x, y) in snake :
                print(answer)
                exit()
            snake.append((x, y))
            if board[x][y] == 1 :
                board[x][y] = 0
            else :
                snake.popleft()
    elif direct == 1 :
        while True :
            answer += 1
            head = snake[-1]
            x, y = head[0], head[1]
            y += 1
            if y >= N or (x, y) in snake :
                print(answer)
                exit()
            snake.append((x, y))
            if board[x][y] == 1 :
                board[x][y] = 0
            else :
                snake.popleft()
    elif direct == 2 :
        while True :
            answer += 1
            head = snake[-1]
            x, y = head[0], head[1]
            x += 1
            if x >= N or (x, y) in snake :
                print(answer)
                exit()
            snake.append((x, y))
            if board[x][y] == 1 :
                board[x][y] = 0
            else :
                snake.popleft()
    else :
        while True :
            answer += 1
            head = snake[-1]
            x, y = head[0], head[1]
            y -= 1
            if y < 0 or (x, y) in snake :
                print(answer)
                exit()
            snake.append((x, y))
            if board[x][y] == 1 :
                board[x][y] = 0
            else :
                snake.popleft()