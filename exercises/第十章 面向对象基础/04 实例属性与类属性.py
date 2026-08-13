class Car:
# 类属性：属于类本身的属性 是所有实例所共享的（所有对象共享的数据或配置）
# 通过：类名.属性 的方式操作   （也可通过对象访问 但遵循实例属性优先原则） 
    wheel=4
    tax_rate=0.1

# 实例属性：实例属性是属于每个具体对象的属性，每个对象都是独立的（各个对象特有的属性）
# 通过：对象名.属性 的方式操作 
    def __init__(self,c_brand,c_name,c_prise):
       self.brand=c_brand
       self.name=c_name
       self.prise=c_prise
       #注意：此处wheel是实例属性
       self.wheel=2
       
    def  total_cost(self,discount,rate):
        return self.prise*discount+self.prise*rate


c=Car("BMW","M5",666666)
cost=c.total_cost(0.9,0.1)
print(f"价格为：{cost}")

# 通过对象名访问属性时候 先访问实例属性 若没有再访问类属性
print(Car.wheel)
print(c.wheel)