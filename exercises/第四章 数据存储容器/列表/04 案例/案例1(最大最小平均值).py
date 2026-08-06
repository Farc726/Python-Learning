# 注意
#1.for循环中range中就已经包含了初始值以及i的递增 也就是步长 不用自己在循环外规定i的初始值 也不用在循环内手动让i递增
#2.键盘输入家的元素都是字符串！！！一定要手动转成int 或者 float！！！！


# 不用额外加 i=0
total=0.0
s=[]
for i in range(0,10):
    # a=float(input("please the element:"))
    # s.append(a)
    s.append(float(input("please the element:")))
    #错了 也不要加i+=1      i 会在循环中以 1 为步长增加是因为 range有了
    total+=s[i]
s.sort()
print(s[0])
print(s[9])
print(total/10.0)

#利用内置语句---另一种求法
print(max(s))
print(min(s))
print(sum(s)/10.0)
print(sum(s)/len(s))