try : 
    array = []
    grade = {"F":0.0, "D0":1.0, "D+":1.5, "C0":2.0, "C+":2.5, "B0":3.0, "B+":3.5, "A0":4.0, "A+":4.5}
    sum = 0
    div = 0
    zero = 0

    for i in range(20) :
        array.append(tuple(input().split()))

    for i in range(20) :
        if array[i][2] == 'P' :
            continue
        else :
            sum += float(grade[array[i][2]])*float(array[i][1])
            div += float(array[i][1])

    print("{:.7}".format(sum/div))
        
except ZeroDivisionError :
    print("0.000000")
