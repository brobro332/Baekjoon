s = input().upper()
sList = list(set(s))
cntList = []

for i in sList :
    cnt = s.count(i)
    cntList.append(cnt)

if cntList.count(max(cntList)) > 1 :
    print('?')
else :
    m = cntList.index(max(cntList))
    print(sList[m])
