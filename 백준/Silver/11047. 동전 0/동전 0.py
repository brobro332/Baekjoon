n, k = map(int, input().split())

a = []
cnt = 0

for i in range(n) :
    a.append(int(input()))

for i in range(n-1, -1, -1) :
    if a[i] <= k :
        cnt += (k//a[i])
        k %= a[i]
        if k == 0 :
            break
print(cnt)