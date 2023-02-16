h, m = map(int, input().split())
c = m - 45

if c < 0 :
    h -= 1
    m = 60 + c
    if h < 0 :
        h = 23
else :
    m -= 45
print(h, m)
