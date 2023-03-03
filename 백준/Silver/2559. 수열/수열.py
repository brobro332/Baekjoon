import sys

n, k = map(int,sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))
cnt = n - (k - 1)
array = []
temp = 0

for i in range(k) :
    temp += target[i]
array.append(temp)

for i in range(cnt-1) :
    temp = temp - target[i] + target[i+k]
    array.append(temp)

print(max(array))
