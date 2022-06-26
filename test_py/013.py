
temp = 0
def fnBox():
    global temp
    temp = 1+3

def fnBox1(arg1):
    arg1 = 5+10

def fnBox2(arg2):
    arg2 = 1+10
    return arg2

print(temp)
fnBox()
print(temp)
tem1 = fnBox1(1)
print(tem1)
tem2 = fnBox2(4)
print(tem2)
