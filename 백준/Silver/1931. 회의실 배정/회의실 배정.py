n = int(input())

a = []
for i in range(n) :
    a.append(list(map(int, input().split())))
a.sort(key = lambda x: (x[1], x[0]))

last = 0
cnt = 0

for start, end in a :
    if start >= last :
        cnt += 1
        last = end
print(cnt)
        
