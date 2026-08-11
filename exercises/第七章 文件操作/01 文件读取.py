# 打开文件
# 写encoding=是因为其本不是第三位置 鼠标放到open函数上去看就知道了
f=open("D:\Python-Project\测试8.11.txt","r",encoding="UTF-8")
print(type(f))

#注意！！！
#文件指针会随读写操作自动后移
#同一文件对象的后续 IO 操作，从当前指针位置继续执行。

#1.读取文件--read(num)
print(f"读取3个字节的结果:{f.read(3)}")
print(f"读取全部内容的结果:{f.read()}")
f.seek(0)

#2.读取文件--readlines() 按行读取 返回列表 每行是列表中的一个元素
lines=f.readlines()
print(type(lines))
print(f"用readlines()读到的内容是：{lines}")
f.seek(0)

#3.读取文件---->readline()
print(f"第一行的数据为：{f.readline()}")
print(f"第二行的数据为：{f.readline()}")
f.seek(0)

#4.读取文件 ---->for 循环
for line in f:
    print(f"每一行是的数据是：{line}")

#关闭文件 -----> f.close()
f.close()

#with open() as f +for 循环  好在 执行完后会自动关闭文件
with open("D:\Python-Project\测试8.11.txt","r",encoding="UTF-8")as f:
    for line in f:
        print(line)
 



