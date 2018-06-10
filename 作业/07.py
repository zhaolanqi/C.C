u = 123456
p = 'abc'
user = int(input('帐号'))
passwd = input('密码')
if user == u and passwd == p:
    print('登录成功')
elif user != u:
    print('帐号不对')
elif passwd != p:
    print('密码不对')

