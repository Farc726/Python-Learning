name1="admin"
number1="666888"
name2="zhangsan"
number2="123456"
name3="taoge"
number3="888666"

name=input("请输入用户名：")
number=input("请输入密码：")

while (name!=name1 or number!=number1)and (name!=name2 or number!=number2)and (name!=name3 or number!=number3):
    if name == "" or number == "":
        print("输入的用户名与密码不可以为空，请重新输入！")
    else:
        print("用户名或密码错误，请重新输入~")

    name = input("请输入用户名：")
    number = input("请输入密码：")

print("登录成功！欢迎进入！")