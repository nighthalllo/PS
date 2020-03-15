n = int(input())
a = list(map(int, input().split()))
nam = list(map(int, input().split()))

num = 0

for i in range(n) :
    if a[i] <= nam[0] :
        num = num + 1
    else :
        if (a[i] - nam[0])%nam[1] == 0 :
            num = num + 1 + int((a[i]-nam[0])/nam[1])
        else :
            num = num + 2 + int((a[i]-nam[0])/nam[1])
        
print(num)