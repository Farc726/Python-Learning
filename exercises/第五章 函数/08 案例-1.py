# 定义一个函数，根据传入的数字，计算该数字阶乘的结果
def function_1(n):
    """计算n的阶乘"""
    if n==1:
        return 1
    else:
        return  function_1(n-1)*n
print(function_1(5))
#递归思想
# n=5
# function_1(4)*5
# n=4
# function_1(3)*4
# n=3
# function_1(2)*3
# n=2
# function_1(1)*2
# function_1(1)=1
# function_1(2)=2
# function_1(3)=6
# function_1(4)=24
# function_1(5)=120