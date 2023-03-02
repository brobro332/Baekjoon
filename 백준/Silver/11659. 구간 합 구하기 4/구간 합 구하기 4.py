import sys

n, m = map(int,sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
tot = [0]
temp = 0

for i in range(n) :
    temp += array[i]
    tot.append(temp)

for i in range(m) :
    a, b = map(int,sys.stdin.readline().split())
    print(tot[b] - tot[a-1])
