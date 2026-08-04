# a=10
# print(type(a))
# b=True
# print(type(b))
# c="hello"
# print(type(c))
# d=None
# print(type(d))
#
# print(type(10.0))
# print(isinstance(10,str))

# s1="he\'llo"
# s2='11\"1'
# s3="""你好\n
# hello"""
# print(s1)
# print(s2)
# print(s3)
# s4="""\t你的暑假真正开始了\n\t迷茫很正常\n\t但是无论如何你都要先前做哦\n加油！！！"""
# print(s4)

# s1="技术大佬"
# s2="持续学习"
# s3="保持好奇心与探索欲"
# print("我会成为"+s1+"的\n为此我要"+s2+"并且"+s3)
# print("我会成为%s的\n为此我要%s并且%s"%(s1,s2,s3))
# print(f"我会成为{s1}的\n为此我要{s2}并且{s3}")

print("欢迎您小智")
password=input("please input your password:")
money=input("please input the money:")
print(f"您取出了{money}，目前余额为：{10000-int(money)}")