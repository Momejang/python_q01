list2 = [(1,2),(3,4),(5,6)]

for x in list2:
    print('##########')
    print(x)
    for y in x:
        print('$$$$$$$$$$$$$')
        print(x)
        print(y)
        if y == 2 or y == 6:
            # print(x)
            # print(str(x[0]) + ' '+ str(x[1]))
