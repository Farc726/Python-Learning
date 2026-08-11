#自己写版
#打开文件
f=open(r"D:\Python-Project\word.txt","r",encoding="UTF-8")
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

#一样的思路with open也可以
with open(r"D:\Python-Project\word.txt","r",encoding="UTF-8") as f:
    contest = f.read()
word_list = contest.split()
number = word_list.count("itheima")
print(f"文本中单词\"itheima\"的个数为：{number}")
    
#一行一行读取版
#熟悉对字符串的操作函数
with open(r"D:\Python-Project\word.txt","r",encoding="UTF-8") as f:
    count=0
    for line in f:
        #由2的更改 --- 本身字符串未变 所以要注意接收！！！！
        line=line.strip()
        #1.现在循环出的line还是字符串--用split("指定分隔符")可以将字符串按照分隔符分割成列表
        words=line.split(" ")
        print(words)#2.但此时 每行最后一个元素还包含换行符 ---- strip()/strip('')--用于去除字符串两端的空白字符或指定字符 在前面还是字符串的时候进行更改
        count+=words.count("itheima")
    print(f"文本中单词\"itheima\"的个数为：{count}")
        
        