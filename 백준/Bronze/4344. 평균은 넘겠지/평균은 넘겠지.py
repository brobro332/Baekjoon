array = []
n = int(input())

for i in range(n) :
    cnt = 0
    sum = 0
    avg = 0
    array = list(map(int, input().split()))
    for j in range(1, len(array)) :
        sum += array[j]
    avg = sum/array[0]
    for k in range(1, len(array)) :
        if avg < array[k] :
            cnt += 1
    print(f"{cnt/array[0]*100:.3f}%")
