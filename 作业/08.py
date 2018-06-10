u = 123456789
p = 123456789
m = 100000000
ur =int(input('帐号'))
pd =int(input('密码'))
if ur == u and pd == p:
    print('登录成功')
    mo = int(input('请输入取钱金额'))
    if m < mo:
        print('没钱取毛线')
    else:
        print('取了%d元,还剩%s元'%(mo,m-mo))
elif ur != u and pd != p:
    print('非法帐号')
