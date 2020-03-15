def resign(schedule, N, good) :
    for i in schedule :
        
        
        

if __name__ == "__main__" :

    N = int(input())
    schedule = []
    good = [0] * (N + 1)
    pay = [0] * (N + 1)

    for i in range(N) :
        num = list(map(int, input().split(" ")))
        schedule.append(num)
    
    for idx_i, i in enumerate(schedule) :
        i.append(i[0] + idx_i)
    print(schedule)

#N일까지 해서 얼마버는지 기준으로