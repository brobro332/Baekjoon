n = int(input())
n_ = n
cnt = 0

while True :
    new_n = (n_ // 10) + (n_ % 10)
    result = (n_ % 10)*10 + (new_n % 10)
    cnt += 1
    if result == n :
        break
    else :
        n_ = result
print(cnt)
        