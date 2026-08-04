# import random
# random_num=random.randint(1,100)
# i=int(input("请输入您猜的数字："))
# while i!=random_num:
#     if i>random_num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     i = int(input("请输入您猜的数字："))
# print("恭喜您！猜对了！")

import random
random_num=random.randint(1,100)

while True:
    i = int(input("请输入您猜的数字："))
    if i>random_num:
        print("猜大了")
    elif i<random_num:
        print("猜小了")
    else:
        print("恭喜您！猜对了！")
        break
print(f"生成的随机数字是：{random_num}")
