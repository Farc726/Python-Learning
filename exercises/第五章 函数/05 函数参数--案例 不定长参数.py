# # 需求：定义函数，根据传入的数据，计算这批数据中的最小值、最大值、平均值。0
# # 基于位置传递
# # def calc_data(*args):
# #     """根据传入的数据，计算这批数据中的最小值、最大值、平均值。"""
# #     max_data=max(args)
# #     min_data=min(args)
# #     avg_data=round(sum(args)/len(args),1)
# #     return max_data,min_data,avg_data

# # data1=calc_data(1,2,3,4,5,6,7,8,9,10)
# # print(data1)

# # data2=calc_data(1,3)
# # print(data2)

# #基于关键字传递
# def calc_data(*args,**kwargs):
#     """根据传入的数据，计算这批数据中的最小值、最大值、平均值。
#     "round"：规定了平均值保留的小数位数
#     "print": True or False决定了是否打印输出
#     """
#     max_data=max(args)
#     min_data=min(args)
#     avg_data=sum(args)/len(args)
# # args收集基于位置传入数据为元组
#     print(args)
#     print(type(args))
# # kwargs收集基于关键字传入数据为字典
#     print(kwargs)
#     print(type(kwargs))
    
#     if kwargs.get("round")!=None:
#         avg_data=round(avg_data,kwargs.get("round"))
#     else:
#         avg_data=round(avg_data,1)
#     if kwargs.get("print"):
#         print(f"max={max_data},min={min_data},avg={avg_data}")
#     return max_data,min_data,avg_data


# data1=calc_data(1,2,3,4,5,6,7,8,9,10,round=3,print=True)
# print()
# data2=calc_data(1,2,3,round=3,print=False)
# print()
# data3=calc_data(1,1,2,print=True)
# print()
# data3=calc_data(1,1,2)

#再来一个案例
# 定义函数 statistic
# 功能：
# 关键字参数支持两个可选配置：
# show：布尔值，True就打印统计结果，False 不打印；不传默认不打印。
# even_only：布尔值，True时只对偶数做统计；不传默认False，统计全部数字。
# 函数返回：(元素数量，元素总和）


def statistic(*args,**kwargs):
    even_only_args=[]
    for num in args:
        if num%2==0:
            even_only_args.append(num)
# 注意访问的时候要加双引号 因为生成字典的键值是字符串类型！
    if kwargs.get("even_only"):
        number=len(even_only_args)
        sum_s=sum(even_only_args)
    else:
        number=len(args)
        sum_s=sum(args)
    if kwargs.get("show"):
        print(f"数量为：{number}   总和为：{sum_s}")
    return number,sum_s

#函数调用时 关键字传参的部分被kwargs收集为字典类型 且键值(show)被自动转化为字符串类型
data1=statistic(1,2,3,4,5,show=True,even_only=True)
print(data1)
print()
data2=statistic(1,2,3,4,5,show=True,even_only=False)
print(data2)
print()
data3=statistic(1,2,3,4,5,show=False,even_only=False)
print(data3)
