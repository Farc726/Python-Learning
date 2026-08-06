# #定义元组---组包
# #最佳
# t1=(1,3,5,7)
# #也可
# t1=1,3,5.7

# t2=(2,4,6,8)
# #基础解包
# a,b,c,d=t2
# print(a,b,c,d)
# #（*）拓展解包
# #*来收集所有剩余的元素，允许我们处理数量不确定的元组（生成列表 便于进一步的处理）
# x,*y,z=t2
# print(x,y,z)
# *p,q=t2
# print(p,q)
# w,*s=t2
# print(w,s)
# a,b,c,*d=t2
# print(a,b,c,d)

#案例一 --- 交换两个变量的值（一行结束）
a=20
b=10

#拆解：相当于组包与解包
# t=a,b
# b,a=t
#合并--一行代码搞定
b,a=a,b

print("a=",a)
print("b=",b)
#案例二 ---- 交换三个变量的值原abc对应cab
a=100
b=200
c=300

c,b,a=a,b,c
print("a=",a)
print("b=",b)
print("c=",c)