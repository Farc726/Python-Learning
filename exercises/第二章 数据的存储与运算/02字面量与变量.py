# python是动态类型语言一个变量可以储存不同类型的数据,(但是项目开发中推荐变量只储存一种类型的数据)
# a = "OK"
# print(a)
# c,d=11,22
# print(c,d)
import tempfile

a=10
b=20
temp=a
a=b
b=temp
print(a,b)


