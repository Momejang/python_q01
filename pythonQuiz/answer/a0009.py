# 화면에 0000011111 출력해주세요
# for 문은 꼭 사용하세요
# print 문을 한번만 사용하세요


# 생각한 정답
string = ''
for x in range(10) :
    if(x > 4) :
        string += '1'
    else :
        string += '0'

print(string)
