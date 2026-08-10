def function1():
    print("a...before")
    function2()
    print("a...after")
def function2():
    print("b...before")
    function3()
    print("b...after")
def function3():
    print("c...")
    
function1()
print("函数执行完毕~")