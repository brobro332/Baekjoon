n = int(input())
array = []
array = (list(map(int, input().split())))
v = int(input())
cnt = 0

for i in range(len(array)) :
    if array[i] == v :
        cnt += 1
print(cnt)
