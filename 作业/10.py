e = 123456789
p = 123456789
U = int(input('帐号'))
P = int(input('密码'))
if U == e and P == p:
    print('登录成功')
    s = input('请选择英雄')
    if s == 'ADC':
        print('后裔','黄忠','虞姬')
    elif s == '肉盾':
        print('亚瑟','程咬金')
    elif s == '法师':
        print('王昭君','妲己')
    elif s == '刺客':
        print('兰陵王','阿珂')
else:
    print('请重新登录')

