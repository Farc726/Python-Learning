class Car:
    def __init__(self,c_brand,c_name,c_prise):
       self.brand=c_brand
       self.name=c_name
       self.prise=c_prise
       
    def  total_cost(self,discount,rate):
        return self.prise*discount+self.prise*rate
# 魔法方法
    def __str__(self):
        return f"{self.brand} {self.name} {self.prise}"
    def __eq__(self, other):
        return self.brand==other.brand and self.name==other.name and self.prise==other.prise
    def __lt__(self, other):
        return self.prise<other.prise
    
    
c1=Car("BMW","M5",666666)
c2=Car("BMW","M5",666666)

print(c1)
print(c1==c2)
print(c1<c2)