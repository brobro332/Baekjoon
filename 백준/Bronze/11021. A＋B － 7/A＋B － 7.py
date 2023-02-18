import sys

t = int(input())
cnt = 1

for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{cnt}: {a+b}")
    cnt += 1
