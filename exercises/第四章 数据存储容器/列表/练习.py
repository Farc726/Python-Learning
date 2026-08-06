#1.用户输入列表中的10个数 后输出这10个数的最小值、最大值、平均值
# s=[]
# for num in range(0,10):
#     s.append(float(input("please input the number:")))
# print(s)
# print(max(s))
# print(min(s))
# print(sum(s)/len(s))

# num_list1=[19,23,54,64,875,20,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]

# #1.
# num_list=num_list1+num_list2
# new_list=[]

# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

#2.
# num_list=[*num_list1,*num_list2]
# new_list=[]
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

#生成1-20的平方列表
# num_list=[i**2 for i in range(1,21)]
# print(num_list)

#提取所有偶数 计算其平方 组成一个新的列表
num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]

new_list=[i**2 for i in num_list if i%2==0]
print(new_list)