n = int(input())
cnt = n

for i in range(n) :
    ch = 0
    a = input().rstrip()
    temp = []
    
    for j in range(1, len(a)) :

        if a[j-1] != a[j] :
            temp.append(a[j-1])
            if j == len(a)-1 :
                temp.append(a[j])
        elif a[j-1] == a[j] and a[j] in temp :
            temp.append(a[j])
    for k in range(len(temp)) :

        if temp.count(temp[k]) > 1 :
            ch = 1

    if ch == 1 :
        cnt -= 1
        ch = 0

print(cnt)

