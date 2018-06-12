u =int(input('请输入数字'))
o = 0
j = 0
i = 0
while i < u:
    #print('输出当前数字%d'%i)
    i+=1
    if i%2 == 0:
        o=o+i
    else:
        j=j+i
print('偶数%s'%o)
print('奇数%s'%j)
print('总和%s'%(j+o))

