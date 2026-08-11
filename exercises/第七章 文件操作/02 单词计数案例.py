#打开文件
f=open("D:\Python-Project\word.txt","r",encoding="UTF-8")
#读取整个文件中的内容
contest=f.read()
# 处理 读取到的字符串以空字符分割
word_list=contest.split()
#对返回的列表进行计数
number=word_list.count("itheima")
#得到结果
print(f"文本中单词\"itheima\"的个数为：{number}")
#关闭文件
f.close()
