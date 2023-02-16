h, m = map(int, input().split())
t = int(input())
c = m + t

if c > 59 :
    while c > 59 :
        c = c - 60
        h += 1
    m = c
    if h > 23 :
        while h > 23 : 
            h -= 24
else :
    m = c
    
print(h, m)
