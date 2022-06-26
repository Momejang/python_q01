#list append(x)
#lsit append(x,y)
#
# str = ['a','b','c']
# str.append('d')
#
# print(str)
#
# str.append((2,'e'))
# print(str)
#
# #len 길이
# print(len(str))
#
# print('aaa {1} {0}'.format('b',1))

arr = [
       ('foo1','bar1'),
       ('foo2','bar2')
      ]
for x in arr:
    print(x)
    for j in x:
        print(j)
