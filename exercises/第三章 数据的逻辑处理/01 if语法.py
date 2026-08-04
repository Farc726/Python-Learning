a=int(input("请输入第一条边长："))
b=int(input("请输入第二条边长："))
c=int(input("请输入第三条边长："))

if a+b>c and b+c>a and a+c>b:
    if a==b==c:
     print("该三角形是等边三角形")
    elif a==b or a==c or b==c:
        print("该三角形是等腰三角形")
    else:
        print("该三角形是普通三角形")
else:
    print(f"{a} {b} {c}这三边无法构成三角形")

