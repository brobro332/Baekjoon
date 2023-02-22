t = int(input())

for i in range(t) :
    r, s = input().split()
    r = int(r)
    s = list(s)
    for j in range(len(s)) :
        for k in range(r) :
            print(s[j],end='')
    print()
