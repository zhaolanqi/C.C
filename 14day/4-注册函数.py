list = []
def zhuce(x,y):
    u = {}
    if len(x) == 11 and x.startswith('1') and len(y) > 6:
        print('注册成功,帐号是%s,密码是%s'%(x,y))
        u ['x'] = x
        u['y'] = y
        list.append(u)
    else:
        print('失败')

x = input('输入手机号')
y = input('输入密码')
zhuce(x,y)

def login(x,y):
    for i in list:
        if u == i['x'] and y == i['y']:
            print('登录成功')
        else:
            print('登录失败')
u = input('请输入帐号')
y = input('请输入密码')
login(x,y)
