'''
s = input('请输入性别:')
if s == '男':
    h = input('请输入身高')
    m = input('请输入财富')
    y = input('请输入颜值')
    if h > '180' and m > '1000' and y > '90':
        print('高富帅')
    else:
        print('稳住，别哭')
if s == '女':
    c = input('请输入皮肤颜色')
    m = input('请输入财富')
    y = input('请输入颜值')
    if c == '白色' and m > '800' and y > '90':
        print('白富美')
    else:
        print('哈哈哈')
'''
d = input('请输入今天星期几')
if d == '1' or d == '2' or d == '3' or d == '4' or d == '5':
    t = input('请输入大致时间')
    if t == '上午':
        s = int(input('请输入时间'))
        if s >= 8 and s < 10:
            print('正在上课')
        elif s >= 10 and s < 12:
            print('玩游戏')
    if t == '下午':
        s =int(input('请输入时间'))
        if s > 14 and s < 17:
            print('正在上课')
        else:
            print('不知道在干什么')
if d == '6':
    print('全天上课')
elif d == '7':
    print('逛街')

