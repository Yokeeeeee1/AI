"""
字典:
    底层:
        字典的底层是hash表,核心靠 hash 值完成两件事：定位存储位置 + 判断键是否重复。
        类似于:先将key hash(key) 然后 将得到的hash值存入 哈希表中,将通过hash值去寻找value 这样时间复杂度为O(1)
    1)字典可以存储多个数据的容器
    元素没有顺序和下标,所以不是序列
    2)字典是可改变对象
    创建与赋值:
        1)用{}创建
        2)使用dict()构造器可以从其他对象创建字典
    字典的获取 修改 添加元素:
        使用[key]获取
    使用update()合并字典
    字典的删除:
        1)使用del d[key]
        2)d.pop(key) 有返回值value
        3)d.clear 清空字典 字典对象是存在的
        如果要删除字典对象,就del 字典名
    字典常用方法:
        dic.keys() 获得所有的key [key1,...,keyn]
        dic.values() 获得所有的value [value1,...,valuen]
        dic.items() 返回类型<class 'dict_items'>,[(key,value),...,()]
    字典的键:
        字典中的值可以是任何Python对象,甚至是字典以及用户自定义类型
        字典中的键可以是Python中其他任意的不可变对象:
            通常是字符串,但也可以是布尔型 整型 浮点型 元组 等
        注意:
            1)元组中只有包含 数字 字符串 这样的不可变参数才可以作为字典中有效键
            2)为什么可变对象不能做 key？（结合 hash 理解）
                列表 list 不能 hash，因为列表内容能随时修改：
                若列表能当 key，存入字典后执行 lst.append(1)，列表变了；
                再次 hash(lst) 得到的数字会完全改变；
                原本根据旧 hash 值存放的坑位找不到了，字典彻底错乱。
            3)如果说使用hash(obj)可以返回对象的hash值,如果返回异常就说明对象不能被hash,
            就代表它肯定不能作字典的键
            4) 不允许一个键对应多个值
            作为键名,例子中出现了两个name,对于这种冲突,Python直接取最后一个值
"""
# 创建
a = {'name': '张三', 'age': 18}
lo1 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
d = dict(lo1)
print(d)
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
d1 = dict(lot)
print(d1)
tol1 = (['a', 'b'], ['c', 'd'], ['e', 'f'])
d2 = dict(tol1)
print(d2)
tol = (('a', 'b'), ('c', 'd'), ('e', 'f'))
d3 = dict(tol)
print(d3)
los = ['ab', 'cd', 'ef']
d4 = dict(los)
print(d4)
tos = ('ab', 'cd', 'ef')
d5 = dict(tos)
print(d5)  # 以上这种例子中的数据叫做双值子序列
d6 = {'ls': 98, 'ds': 99, 'os': 100}
d6['ls'] = 100
print(d6)
# 合并字典
d6.update(a)
print(d6)
# 删除
# del d6['ls']
# print(d6)  # {'ls': 100, 'ds': 99, 'os': 100, 'name': '张三', 'age': 18}
# pop = d6.pop('ds')
# print(pop)
# print(d6) # {'ds': 99, 'os': 100, 'name': '张三', 'age': 18}
# d6.clear()
# print(d6) # {}
print(d6.items())
print(d6.keys())
print(d6.values())
atuple = 1,'a'
dic = {atuple:3}
print(dic)

# 生成一个游字典中的值有大到小排序得到的列表
# sorted方法
d7 = {1:1,2:2,3:3,8:8,0:0}
values= d7.values()
values = sorted(values,reverse=True)
print(values)
# sort()方法
d8 = {1:1,2:2,3:3,8:8,0:0}
lvalues = list(d8.values())
print(lvalues)
lvalues.sort(reverse=True)
print(lvalues)