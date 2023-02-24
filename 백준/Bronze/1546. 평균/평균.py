n = int(input())
a = list(map(int, input().split()))
tot= 0
avg = 0

sol = sorted(a)
maxi = sol[n-1]

for i in range(len(sol)) :
    tot += sol[i]/maxi*100

avg = tot / n
print(avg)
