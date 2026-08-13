# # 定义类----->动态为对象添加属性 （不推荐）
# class Car:
#     pass

# # 创建对象
# c1=Car()
# c1.brand="BEW"
# c1.name="M5"
# c1.prize=500000
# # __dict__ 是用户自定义实例的一个特殊属性，用于以字典的形式存放对象的属性
# print(c1.__dict__)
# print(c1)
# print(c1.brand)

# 定义类
class Car:
#__init__是初始化的方法，会在对象创建时自动调用 可以用该方法在对象中创建属性
# self相当于this指针
    def __init__(self,c_brand,c_name,c_prize):
        self.brand=c_brand
        self.name=c_name
        self.prize=c_prize
        
# 创建对象
c1=Car("BMW","M5",500000)
print(c1.__dict__)
print(c1.brand)