n = int(input())
empty = ' '

for i in range(1, n+1, 1) :
        print(" "*(n-i)+"*"*i, end='')
        print()
