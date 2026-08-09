#有关字符串
s="hello-python-hello-world"
print(s)

for element in s:
    print(f"{element} ",end="")

print()
print(s.find('h'))
print(s.upper())
print(s.replace("-","$"))
print(s.startswith("h"))
print(s.startswith("q"))

#有关元组
#其他特点与列表基本一致 不同点为元组不可以修改
t1=(1,2,3)
print(type(t1))
print(t1)

#解包
a,b,c=t1
print(a,b,c)
#组包,上

#交换值    abc--->cab
a=1
b=2
c=3

# t=a,b,c
# c,b,a=t

c,b,a=a,b,c
print(a,b,c)

