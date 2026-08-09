dict1={"jack":701,"Alice":547,"mary":620,"mary":111}
print(type(dict1))
#key不可以重复 若重复了相对靠后的值会将前面的值覆盖掉
print(dict1)

# dict2={"jack":701,"Alice":547,"mary":620,[1,2,3]:123}
# print(dict2)

#获取值
print(dict1["jack"])
dict1["Alice"]=647
print(dict1)
print(dict1["Alice"])

