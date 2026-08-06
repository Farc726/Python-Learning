s="python"
print(s[0:-2:1])
print(s[:3:])

#s[4]="x"字符串不可进行修改操作
print(s)

#可迭代性(可以遍历后输出)
for element in s:
    print(f"{element} ",end="")