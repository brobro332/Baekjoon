n = int(input())
array = []
if n == 1 :
    array.append(int(input()))
else :
    array = list(map(int,input()))
print(sum(array))
