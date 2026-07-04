"""
while循环:
    语法:
        while 条件:
            loop code
    死循环:
        while True:
            ...

for循环:
    语法:
        for item_var in iterable   # iterable 是可迭代对象
            code to process item_var
for...in...的使用

break,continue,pass:
    1)break:
        在循环中使用break可以立即终止整个循环,不论是否完成循环的所有迭代
    2)continue:
        可以跳过当前迭代直接进入下一次迭代
    3)pass:
        只是一个占位符,来保证代码结构完整,不需要做任何实际操作



enumerate可以把一个list变成索引-元素对儿,这样就可以在for循环中同时迭代索引和元素本身
"""
x = 1
sum = 0
while x <= 100:
    sum = sum + x
    x += 1

print(sum)
print("="*40)
sum = 0
for i in range(1,101):
    sum = sum + i

print(sum)


# enumerate()
name_list = ["李磊","你好"]
for i , name in enumerate(name_list):
    print(i,name) #0 李磊
                  #1 你好

# break
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        break
    print(num)
print("="*40)
# # continue
# nums = [1,2,3,4,5]
# for num in nums:
#     if num == 3:
#         continue
#     print(num)
# print("="*40)
# user = input("请输入一串数字:")
# dic = {}
# for i in user:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(dic)
# print("="*40)

import re

story = '''the wolf swallowed a bone by mistake, which wa
he ran around looking for a doctor.
he met the Osprey and asked him to take out the bone.
the Osprey put her head into the wolf's throat and took o
sked the wolf for a good reward.
the wolf replied, "Hey, friend, you can take it back safe
uth.
isn't it satisfied? How can you pay?"'''

# 第一步：把所有换行换成空格，消除换行
one_line = story.replace('\n', ' ')
# 第二步：按 . ? ! 分割句子（保留分隔符）
sentences = re.split(r'([.!?])', one_line)
processed = []
# 遍历成对的句子+分隔符
for i in range(0, len(sentences), 2):
    sent = sentences[i].strip()
    sep = sentences[i+1] if i+1 < len(sentences) else ''
    if sent:
        # 句子首字母大写，其余小写
        new_sent = sent.capitalize()
        processed.append(new_sent + sep)
# 拼接所有句子，去掉多余空格
result = ' '.join(processed)
# 清理连续空格
result = re.sub(r'\s+', ' ', result).strip()
print(result)