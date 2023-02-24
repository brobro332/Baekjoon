n = list(input().strip())
cnt = 0

if len(n) == 0 :
    print(0)
else :
    for i in n :
        if i == ' ' :
            cnt += 1
    print(cnt+1)
