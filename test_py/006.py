#try catch?
#try except eles finally

intArr = [0,1,2,3,4,5,6,7,8,9]
intArr2 = [x for x in range(9)]
for x in intArr2:
    try :
        result = x % 3
        print(result)
        if(result == 0) :
            print('결과 : '+str(result))
        else :
            prin('결과 : '+str(result))
    except :
        print('예외가 발생하였습니다')
    else:
        print('try 에 넣고싶지 않은 부분, except 가 발생하지 않았다면 실행된다')
    finally:
        print('항상출력')
