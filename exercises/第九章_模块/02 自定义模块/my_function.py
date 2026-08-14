#__all__卸载模块里面！
# 关于*
#__all__=["function1","QUESTION"]
# 常量
PI=3.1415926
QUESTION="你该如何度过暑假~"

# 函数
def function1():
    print("*"*20)
    
def function2():
    print("-"*20)

def function3():
    print("$"*30)
    
#测试函数
#__name__:
# python中的内置变量 ，表示当前模块的名字（直接运行当前模块，__name__的值为__main__）
# 当该模块被导入时 __name__的值为模块名称
if __name__=="__main__":
    function1()
    print(PI)
    



# 执行当前文件则会执行如下代码 当作模块导入则如下代码不执行
# 简化写法 直接写main后回车