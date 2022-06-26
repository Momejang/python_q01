#제네레이터 라는건 이터레이터를 직접 만들때 사용한다, 사용하는곳이 많지는 않다

#제네레이터 , 일드
#generator 제네레이터
#yield 일드

def 함수이름():
    print('1번 출력')
    yield
    print('2번 출력')
    yield

호출함수 = 함수이름()
# next(호출함수)
# print(' 공백 ')
# next(호출함수)

for x in 호출함수:
    print(x)
