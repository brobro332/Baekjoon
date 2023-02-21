array = [0] * 30

for i in range(28) :
    a = int(input())
    array[a-1] = 1

for j in range(30) :
    if array[j] == 0 :
        print(j+1)
