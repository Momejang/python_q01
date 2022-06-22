# for문 을 활용할세요
# 문자 함수를 활용하세요
# python 에는 o 가 존재합니다
# WELCOME 에는 해당문자가 존재하지 않습니다
# Tutorial 에는 o 가 존재합니다
# tistory 에는 o 가 존재합니다
# github 에는 해당문자가 존재하지 않습니다

stringArr = ['python','WELCOME','Tutorial','tistory','github']

for x in stringArr :
    if(x.find('o') > -1) :
        print(f'{x} 에는 o 가 존재합니다')
    else :
        print(f'{x} 에는 해당문자가 존재하지 않습니다')
