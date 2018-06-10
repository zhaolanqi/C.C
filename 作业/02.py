y = int(input('请输入年'))
if y % 4 == 0 and y % 100 != 0:
    print('润年')
elif y % 400 == 0:
    print('润年')
else:
    print('平年')
