n = input()
array = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0

for i in n :
    for j in range(len(array)) :
        if i in array[j] :
            t += j
            break
print(t)
