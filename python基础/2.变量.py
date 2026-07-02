# 变量
# 1.方便引用内存中的值为它起的名字
# 普通赋值
int_example = 1
str_example = 'hello world'
# 增量赋值
int_example += 1
print(int_example)
str_example += ('\thello')
print(str_example)
# 多重赋值
x, y = 1, 2
print(x, y)
# 命名规则: 数字不能开头 关键字不能开头 预留字也不能用
c = id(1000)
d = id(1000)
print(c == d)
"""
小数池:
-5 ~ 256 永久缓存，任何场景 id 都相等
大于 256 或小于 - 5 的数字，是否同地址完全取决于编译优化 + 代码书写位置
"""