"""
结构:
    if-elif-else 语句

多重比较:
    使用布尔操作符and or 或者 not 连接来决定最终的表达式的布尔取值
    表达式先计算后比较
    避免混淆的办法加圆括号
条件表达式(三元操作符):
    语法: X if C else Y
下面的情况会被认为是False:
    bool            False
    null类型         None
    整型              0
    浮点型            0.0
    空字符串           ''
    空列表             []
    空元组             ()
    空子典             {}
    空集合            set()
其余都为True
注意:保证同样逻辑层次的语句有相同的缩进量
"""
today = input("请输入一个数字(1-7):")
if today == "1":
    print("今天是星期一")
elif today == "2":
    print("今天是星期二")
elif today == "3":
    print("今天是星期三")
elif today == "4":
    print("今天是星期四")
elif today == "5":
    print("今天是星期五")
elif today == "6":
    print("今天是星期六")
elif today == "7":
    print("今天是星期日")
else:
    print("请输入正确的数字")
print("=" * 40)
# 三元操作符
x, y = 3, 4
small = x if x > y else y
print(small)
print("=" * 40)
s, t = 3, 4
small = (t, s)[s < t]
print(small)
