n = int(input())
array = list(map(int, input().split()))
sum = 0

array.sort()

for i in range(n) :
    for j in range(n) :
        if j <= i :
            sum += array[j]
print(sum)
