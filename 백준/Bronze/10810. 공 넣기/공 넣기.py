n, m = map(int, input().split())
array = [0] * n

for x in range(m) :
    i, j, k = map(int, input().split())
    while True :
        array[i-1] = k
        i += 1
        if i-1 > j-1 :
            break
for a in range(n) :
    print(array[a], end=' ')
