#常见方法
dict1 = {"小曾": 675, "李想": 608, "李琪": 478, "小唐": 545, "祖国": 429}

#添加
dict1["小红"]=567
print(dict1)
#修改
dict1["小曾"]=666
print(dict1)

#删除
del dict1["小曾"]
print(dict1)
print(dict1.pop("李想"))
print(dict1)

#查询
print(dict1["李琪"])
print(dict1.get("李琪"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
