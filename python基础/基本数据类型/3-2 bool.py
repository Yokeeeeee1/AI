"""
bool:

# 使用内建函数bool()返回布尔对象
# 非空字符串都是True 相反就是False
# 运算符 : 优先级 :not > and > or
转换工厂函数:
    int()
    float()
    bool()
转换是表现,实质创建新的对象
"""
print(bool('123'))
print(bool(''))
# 功能函数
a = pow(2, 3)  # 2的3次方
print(a)
# 四舍五入
b = round(3.1415926, 2)  # 可以用第二参数指定精确到小数点后几位  第二参数为空时,向上取整还是向下取整和奇偶性有关
# 奇数向上,偶数向下
print(round(3.5))
print(round(4.5))
print(b)
