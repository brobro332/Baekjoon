array = []
s = input()


a = 97
while True :
    array.append(chr(a))
    a += 1
    if a > 122 :
        break

for i in array :
    print(s.find(i), end=' ')
