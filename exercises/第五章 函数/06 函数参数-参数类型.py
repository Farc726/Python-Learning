#普通参数
#函数
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calc(x,y,oper):
    return oper(x,y)

print(calc(4,2,add))
print(calc(4,2,subtract))

