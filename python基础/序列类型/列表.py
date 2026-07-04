"""
列表:
    列表中元素可以为不同类型
    是可变对象
    可以直接对原始列表进行修改:添加 删除 覆盖
    存取的是每个元素的指向关系
创建列表:
    方法1: 用[]括起来
    方法2: 用内置list()函数
"""
lower_alphas = list('abcdefgh')
upper_alphas = list('abcdefgh'.upper())
alphas = [lower_alphas, upper_alphas]
print(alphas)
