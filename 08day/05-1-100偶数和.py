i = 0
r = 0
while i<=100:
    if i % 2 == 0:
        #print(i)
        r += i
        i += 2
        print('1-100偶数和%s'%r)
a=1
b=0
while i<=100:
    if a % 2 !=0:
        b += a
        #print(a)
        #print(b)
        a += 2
        print('1-100奇数和%s'%b)
