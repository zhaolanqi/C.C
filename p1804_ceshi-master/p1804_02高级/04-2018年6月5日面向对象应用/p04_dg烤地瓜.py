#-*-coding:utf-8-*-

#烤地瓜   对象  类
# 对象： 每一个  烤出来的地瓜  对象
# 过程：  烤地瓜的 ，整个流程

class SweetPotato:
    def __init__(self):
        self.info = '生地瓜'
        self.lever = 0
        self.Seasoning = []   # 保存 烤地瓜添加的 调料
    # 3分钟 半生不收  5分钟 刚刚好   6分钟 火大   8 糊了
    def cook(self, t):
        self.lever += t
        if self.lever >= 8:
            self.info = '烤糊的黑地瓜'
        elif self.lever >= 6:
            self.info = '火大的黄地瓜'
        elif self.lever >= 5:
            self.info = '新鲜出炉的上好烤地瓜'
        elif self.lever >= 3:
            self.info = '半生不熟的硬地瓜'
        else:
            self.info = '生地瓜'
    def AddSeasoning(self, Seasoning):
        self.Seasoning.append(Seasoning)

    def __str__(self):
        for i in self.Seasoning:
            self.info +=  i + ','
        self.info = self.info.strip(',')
        return '当前的地瓜状态是：%s, 烤制此地瓜一共使用了 %d 分钟时间  '%( self.info, self.lever)



dg01 = SweetPotato()
print (dg01.info)
dg01.cook(3)
print (dg01.info)
dg01.cook(2)
print (dg01.info)
dg01.cook(1)
print (dg01.info)
dg01.AddSeasoning('辣椒油')
dg01.AddSeasoning('孜然')
dg01.AddSeasoning('蜂蜜')
dg01.AddSeasoning('黄油')

print(dg01)
