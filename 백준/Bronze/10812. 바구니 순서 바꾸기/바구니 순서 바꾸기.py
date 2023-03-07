array = []
temp = 0

n, m = map(int, input().split())

for a in range(1, n+1) :
    array.append(a)
for b in range(m) :
    i, j, k = map(int, input().split())
    array[i-1:j] = array[k-1:j] + array[i-1:k-1]
for c in array :
    print(c, end=' ')
