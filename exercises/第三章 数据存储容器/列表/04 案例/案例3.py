# #生成1-20的平方列表
# #方法一：传统方法
# s=[]
# for i in range(1,21):
#     s.append(i**2)
# print(s)
# #方法二：列表推导式----->语法格式：[要插入的值 for i in 序列/列表]
# num_list2=[i**2 for i in range(1,21)]
# print(num_list2)

#提取所有偶数 计算其平方 组成一个新的列表
#方法一:传统方法
# num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
# list=[]
# for num in num_list:
#     if num%2==0:
#         list.append(num)
# new_list=[i**2 for i in list]
# print(new_list)


#方法二：列表推导式进阶----->语法格式：[要插入的值 for i in 序列/列表 if 条件]
num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)
