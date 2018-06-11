import random
i = 0
while i <= 10:
    pc = random.randint(1,100)
    #print(pc)
    u = int(input('请输入您猜的数字'))
    if u > pc:
        print('猜大了ovo')
    elif u < pc:
        print('猜小了ovo')
    else:
        print('猜对啦')
        break
i += 1
