n, x = map(int, input().split())
array = []
array = (list(map(int, input().split())))

for i in range(len(array)) :
    if array[i] < x :
        print(array[i], end=' ')
