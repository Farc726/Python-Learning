#进行 JOSN 数据与 python 字典的相互转换
import json
# 将字典转化为json格式
data_1={"name":"Jack","age":18}
data_1=json.dumps(data_1)
print(type(data_1))
print(data_1)
# 将列表转换位json格式
# 在转化中文时 防止乱码 加一个ensure_ascii=False 不使用ascii码转换
data_2=[{"name":"Jack","age":18},{"name":"张三","age":20}]
data_2=json.dumps(data_2,ensure_ascii=False)
print(type(data_2))
print(data_2)
# 将json格式数据转换为字典(因其本质是字符串)
data_3='{"name":"Jack","age":18}'
data_3=json.loads(data_3)
print(type(data_3))
print(data_3)
# 将json格式数据转换为列表
data_4='[{"name":"Jack","age":18},{"name":"张三","age":20}]'
data_4=json.loads(data_4)
print(type(data_4))
print(data_4)

#注意！！！JSON语法规定：JSON内部字符串必须使用双引号 不允许使用单引号 所以python字符串外层使用单引号可以避免引号冲突