
x = input('x 를 입력하세요')
y = input('y 를 입력하세요')
z = input('z 를 입력하세요')
temp1 = input('첫번째 연산자를 입력하세요')
temp2 = input('두번재 연산자를 입력하세요')

def operation(arg1, arg2, oper1):
    # 사칙연산
    return int(arg1) + int(arg2)

resultVar1 = operation(x,y,temp1)
resultVar2 = operation(resultVar1,z,temp2)
print(resultVar2)
