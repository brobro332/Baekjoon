array = []
cnt = 0

for i in range(9) :
    array.append(int(input()))
a = max(array)
print(a)
for i in array :
    cnt += 1
    if i == a :
        break
print(cnt)
