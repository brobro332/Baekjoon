n = int(input())
result = ""
sp = " "

for i in range(1, n+1) :
    for j in range(i, n) :
        result += sp
    for k in range(1, i*2) :
        result += "*"
    result += "\n"

for i in range(n, 1, -1) :
    for j in range(i, n+1) :
        result += sp
    for k in range(i*2, 3, -1) :
        result += "*"
    result += "\n"
    
print(result)

