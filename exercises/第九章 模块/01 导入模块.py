# 一般导入模块语句放在py文件的最上方

# 导入模块(模块名.功能名调用)
# import random
# for i in range(1,101):
#     print(f"{random.randint(1,100)} ",end="")

import random as rd
for i in range(1,11):
    print(rd.randint(1,10))

print()


# 导入模块中的功能
from random import randint
for i in range(1,6):
    print(randint(1,6))
print()

from random import *
for i in range(1,6):
    print(randint(1,6))