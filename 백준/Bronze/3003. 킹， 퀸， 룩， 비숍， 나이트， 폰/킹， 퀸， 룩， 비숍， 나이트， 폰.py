data = list(map(int, input().split()))
full = [1, 1, 2, 2, 2, 8]

for i in range(len(full)) :
    print(full[i] - data[i], end=' ')
