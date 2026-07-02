# 1 对象 三个特征: 类型 值 身份
# 1.1 类型
# 1.1.1 通过type()方法来查看类型
print(type(123))
print(type('123'))
# 1.1.2 使用isinstance()来验证类型 返回值是bool
print(isinstance(123, int))
print(isinstance('123', (str,int,float)))

# 1.2 值
# 操作符:<,>,<=,>=,==,!= 返回值: bool
print(1<2)
print(1>2)
print("a" == "a")
# 比较的是编码的大小
print("a" <= "b")

# 1.3 身份 每个对象都有唯一的身份标识,可以使用内建函数id()来查看,所得值可以理解为内存地址
print(id(123))
# 1.3.1 身份比较  若是两个对象在内存中相同,那么它们的身份比较结果为True
print(id(123) == id(123))
# 1.3.2 对象的引用
a = 123
b = 123
print(id(a) == id(b))
