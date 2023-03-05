n, m = map(int, input().split())
array = []

for i in range(1, n+1) :
    array.append(i)

for i in range(m) :
    a, b = map(int, input().split())
    array = array[:a-1] + array[a-1:b][::-1] + array[b:]

for i in range(len(array)) :
    print(array[i], end=' ')
