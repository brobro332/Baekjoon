x = int(input())
n = int(input())

tot = 0


for i in range(n) :
    a, b = map(int, input().split())
    tot += a*b
   
if tot == x :
    print("Yes")
else :
    print("No")
