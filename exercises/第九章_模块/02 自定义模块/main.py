# # 导入模块
# import my_function

# # 执行模块中的功能
# my_function.function1()
# my_function.function2()
# my_function.function3()
# print(my_function.PI)
# print(my_function.QUESTION)

# # 导入模块中的功能
# from my_function import function1
# function1()

# # 导入模块中的所有功能
# from my_function import *
# print(QUESTION)
# function3()
# function1()
# function2()

# 关于*
from my_function import *
function1()
print(QUESTION)

# 会警告 因为* 现在不包含  function2()----->看模块中有没有指定__all__  若没有就是全部
#function2()
