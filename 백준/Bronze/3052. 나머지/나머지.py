import sys
input = sys.stdin.readline
array = [0]*42
cnt = 0

for i in range(10) :
    temp = int(input())
    temp %= 42
    array[temp] = 1

print(array.count(1))

