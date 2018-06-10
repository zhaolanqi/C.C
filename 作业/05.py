s = input('请输入性别:')
if s == '男':
    h = input('请输入身高')
    m = input('请输入财富')
    y = input('请输入颜值')
    if h > '180' and m > '100000' and y > '90':
        print('高富帅')
    elif h < '160' and m < '100' and y < '60':
        print('矮穷挫')

