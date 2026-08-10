# #计算圆面积的函数
# def s_circle(r):
#     area=3.14*r*r
#     return area

# r=float(input("请输入圆的半径："))
# print(f"该圆的面积为{s_circle(r):.2f}")

# def s_jvxing(l,d):
#     area=l*d
#     return area
# l=float(input("请输入长方形的长:"))
# d=float(input("请输入长方形的宽："))
# print(f"该长方形的面积为{s_jvxing(l,d):.2f}")

#在一个函数中计算圆的周长和半径
def c_s(r):
    """
    该函数是用来根据圆的半径来计算圆的周长和面积
    r:圆的半径
    """
    
    c=2*3.14*r
    area=3.14*r*r
    return c,area
print(c_s(1))
print(type(c_s(1)))
#看函数的说明文档
help(c_s)

r=float(input("请输入圆的半径："))
c,s=c_s(r)
print(f"该圆的周长为{c:.2f}")
print(f"该圆的面积为{s:.2f}")


