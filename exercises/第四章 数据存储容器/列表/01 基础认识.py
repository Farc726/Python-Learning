#列表的基础操作
#定义列表
s=[56,90,88,65,90,"A","hello",True]
print(type(s))
#获取
print(s[0])
print(s[-8])

#修改
s[5]="ABC"
print(s)

# 索引超出范围 s[10]=1

#删除
del s[6]
print(s)

#挨个输出
for i in range(0,7):
    print(f"{s[i]} ",end="")
print()

#更常用
for i in s:
    print(f"{i} ",end="")