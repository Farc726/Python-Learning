class Car:
    def __init__(self,c_brand,c_name,c_prise):
       self.brand=c_brand
       self.name=c_name
       self.prise=c_prise
       
    def  total_cost(self,discount,rate):
        return self.prise*discount+self.prise*rate

c=Car("BMW","M5",666666)
cost=c.total_cost(0.9,0.1)
print(f"价格为：{cost}")