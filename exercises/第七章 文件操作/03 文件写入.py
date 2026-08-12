import time
# 打开不存在的文件
f=open("D:\Python-Project\测试8.12.txt","w",encoding="UTF-8")
# 对文件进行写入
f.write("今天练肩臂！")
# 测试一下 如果没关闭 且 没刷新
# 手动刷新
f.flush()
# time.sleep(10)
# 关闭文件
f.close()

#打开一个已经存在的文件 
f=open("D:\Python-Project\测试8.12.txt","w",encoding="UTF-8")
# 写入 刷新
f.write("你好你好你好~")
f.flush()
#关闭
f.close()

# 注意在用w 打开文件时 每次写入都会清空文件的内容 
