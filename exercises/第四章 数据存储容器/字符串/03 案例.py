s=input("please input your e_mail:")

#方式一：
if s.count('@')==1 and s.count('.')>=1:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

#方式二：通过 in 运算符 判断字串是否存在于字符串中
if s.count('@')==1 and "."in s:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
