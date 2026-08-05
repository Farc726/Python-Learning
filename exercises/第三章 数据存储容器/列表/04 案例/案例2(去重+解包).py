num_list1=[19,23,54,64,875,20,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

#合并列表(尽量不用下标 容易很混乱)
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的原始列表：",num_list1)

#合并列表简化版1
#解包：将列表这一类容器解开成一个一个独立的元素
#组包：将多个值合并到一个容器
#num_list=[*num_list1,*num_list2]

#合并列表简化版2
num_list=num_list1+num_list2
print("合并后的原始列表：",num_list)

#去重
new_list=[]# 去除重复后的列表

for num in num_list:
    #判断new_list中是否存在num元素
    if num not in new_list:#判断元素是否存在于列表中  in运算符 存在则返回True 否则返回False
        new_list.append(num)
print("去除重复之后的列表：",new_list)


#精简版
# num_list1=[1,2,3,4,5]
# num_list2=[4,5,6,7,8,9]

# num_list=num_list1+num_list2
# #num_list=[*num_list2,*num_list1]
# print("合并后的原始列表：",num_list)

# new_list=[]
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)

# print("去重后的列表：",new_list)
