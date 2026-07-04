"""
# 序列是一种容器类型,存储多个对象
# 创建序列: list() tuple() dict() set()
1.序列中的每个元素都有自己的索引位置
2.序列都可以进行的操作包括 成员检查 加 乘 索引 切片
3 python中内置的序列类型有 str,列表,元组,字典,集合
"""
# 成员关系操作符 (in | not in)
print('a' in 'abc')
print('a' not in 'abc')
# 连接操作符(+)
print('a' + 'b')
# 重复操作符(*)  用以将序列重复指定的次数  s*n 当n<0时,都按n=0处理 返回一个空字符串
print('a' * 3)
# 切片操作符([] | [start_index:end_index] | [start_index:end_index:step_length]) 左闭右开  正数从0开始计数  从左往右  负数从-1开始计数 从右往左
# 操作索引时,步长的执行顺序要和开始和结束索引的顺序一致
str_example = 'helloworld'
print(str_example[2])
print(str_example[2:5])
print(str_example[:5])
print(str_example[::2])
print(str_example[len(str_example)-1:])