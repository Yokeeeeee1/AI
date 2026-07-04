"""
推导式:
    概念:
        是Python内置的非常简单却强大的可以用来常见数据的生成式
        避免冗余代码
    列表推导式:
        语法:
            [expr for item_var in iterable]
        改语法的核心是for 循环:
        拓展语法:
            [expr for item_var in iterable if cond_expr]
            [expr if cond_expr else else_expr for item_var in iterable]

"""
# 列表推导式
a = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(a)
b = [i ** 2 if i % 2 == 0 else -i for i in range(1, 11)]
print(b)
# for x in 'ABC':
#     for y in 'abc':
#         for z in 'xyz':
#             print(x + y + z)
c = [x + y + z for x in 'ABC' for y in 'abc' for z in 'xyz']
print(len(c))

# print([ss[::-1] for ss in ['green', 'red', 'blue']])
# 100以内17的倍数:
print([i for i in range(100) if i % 17 == 0])
# 1-100中,3的倍数保持不变,其他的数取相反数
print([i if i%3 ==0 else -i for i in range(1,101)])
# 将字符串中的字母变为小写,其余元素不变
L = ['Hello','World',18,'Apple',None]
print([s.lower() if isinstance(s,str) else s for s in L])