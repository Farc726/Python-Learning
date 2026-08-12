# 把写入的"w"--->"a"即可
f=open("D:\Python-Project\测试8.12.txt","a",encoding="UTF-8")
f.write("看看状态，明天练腹？")
f.write("\n换行写")
f.close()