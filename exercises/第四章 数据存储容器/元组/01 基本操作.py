#元组-tuple
t1=(80,95,78,50,76,80,85,20)

print(t1)
print(type(t1))
print(t1[0])
print(t1[-2])
print(t1.count(80))
print(t1.count(0))
print(t1.index(95))
print(t1.index(80))
#切片
print(t1[0:3:1])


t2=()
print(t2)
print(type(t2))
#注意点：
#定义单个元素的元组，单个元素之后，需要加上逗号，否则是int类型
t3=(100)
print(t3)
print(type(t3))#int 

t4=(100,)
print(t4)
print(type(t4))