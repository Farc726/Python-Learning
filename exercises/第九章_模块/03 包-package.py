# 1.导入模块
# import utils.my_func
# utils.my_func.function1()

# from utils import my_var
# print(my_var.QUESTION)

# from utils import *
# my_func.function2()

# 2.导入模块中的功能
# 相对路径：从当前文件夹所在目录下开始查找
from utils.my_func import function2
function2()
# 绝对路径：从项目的根目录下开始查找
from 第九章_模块.utils.my_var import PI
print(PI)

