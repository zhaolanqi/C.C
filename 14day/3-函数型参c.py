def jsq(x,y,z):
    if z == '+':
        print(x+y)
    elif z == '-':
        print(x-y)
    elif z == '/':
        if y != 0:
            print(x/y)
        else:
            print('不合法')
    elif z == '%':
        print(x%y)
    elif z == '**':
        print(x**y)
    elif z == '*':
        print(x*y)
x = float(input('请输入X值'))
z = input('请输入运算符')
y = float(input('请输入Y值'))
jsq(x,y,z)
