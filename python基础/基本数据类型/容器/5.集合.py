"""
集合
    概念:
        和数学中的概念是一样的
        可以对其进行 交 并 差 补 等操作
    类型:
        1) 可变集合(set)
        2) 不可变集合(frozenset)
            frozenset的核心约束是：对象创建后，自身内部的哈希表结构、元素集合永远不能改动，目的是保证哈希值永久稳定，能作为字典 key、普通 set 的元素
    创建集合:
        1)使用{}将一系列逗号隔开的值包裹起来创建集合
        2)使用内建函数set()和frozenset()构造器创建集合
    集合类型操作符和内建方法:
        标准类型操作符:
            1)成员关系判定:in | not in
            2)集合等价/不等价: = | !=
            3)子集/超集判定: < | <= | > | >=
        内建方法:
            s.issubset(t)     如果s是t的子集,返回True
            s.issuperset(t)   如果s是t的超集,返回True
            s.union(t)        返回一个新集合(并集)
            s.intersection(t) 返回一个新集合(交集)
            s.difference(t)   返回一个新集合(差集)
            s.symmertric_difference(t) 返回一个新集合(补集)
            s.copy()            返回一个新集合,它是s的浅复制
            s.pop()             删除s中任意一个对象,并返回
            s.clear()           删除集合s中的所有元素
    特点:
        1)集合中元素不可重复
"""
# 创建
a_set = {1, 2, 3}
b_set = set([1, 2, 3])
c_set = frozenset([1, 2, 3])
print(a_set)
print(b_set)
print(c_set)
# =======================================================================================
# 集合类型操作符和内建方法
print(set('book') <= set('paper'))
print(a_set < b_set)
print(1 in a_set)
# ========================================================================================
# 交 并 插 补
# s = set('abcde')
# t = set('defgh')
# print(s | t)   # 并集
# print(s & t)   # 交集
# print(s - t)   # 差集
# print(s ^ t)   # 补集 两个集合中独立存在的,去除两个结合都有的元素
# 集合类型操作符(可变集合)
print("===============================")
s = set((1, 3, 5, 7))
t = {5, 7, 9, 0}
s |= t
print(s)
s &= t
print(s)
s -= t
print(s)
s ^= t
print(s)
# 更新集合
print("=" * 40)
myset = {1, 2, 3, 4}
myset.add(5)
print(myset)
# 更新集合
newset = {4444, 1111, 2222}
myset.update(newset)
print(myset)
# 删除
myset.remove(4444)
print(myset)
print("=" * 40)
# 借助集合的特点去重
lists = [2, 3, 5, 3, 6, 3, 2, 4, 8, 0]
# print(sorted(list(set(lists)), reverse=True))
l= list(set(lists))
l.sort(reverse=True)
print(l)
