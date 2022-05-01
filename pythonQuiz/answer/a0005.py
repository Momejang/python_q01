# for 문을 사용해서 숫자가 2 와 6이 사용된 내용을 출력하세요
# 출력내용
# (1, 2)
# (5, 6)
list = [(1,2),(3,4),(5,6)]

for x in list:
    print('##########')
    print(x)
    for y in x:
        print('$$$$$$$$$$$$$')
        print(x)
        print(y)
        if y == 2 or y == 6:
            print(x)
            # print(str(x[0]) + ' '+ str(x[1]))

#
