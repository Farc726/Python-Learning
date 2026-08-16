try:
    print("=========")
    #print(name)
    #print(1/0)
    #print("abc"[10])
    print("abc".hello)
    print("=========")
except NameError as e:
    print("名字不存在,异常信息：",e)
except ZeroDivisionError as e:
    print("0 不能做被除数,异常信息：",e)
except IndexError as e:
    print("索引错误,异常信息：",e)
# 捕获所有类型的异常
except Exception as e:
    print("程序运行异常，请联系管理员~",e)

#主要是做资源释放之类的工作
# 无论程序是否正常运行finally代码块中的代码都会运行
finally:
    print("释放资源")