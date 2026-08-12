# 以只读的方式打开初始账单文件
f=open("D:\Python-Project\8.12-bill.txt","r",encoding="UTF-8")
# 以w的方式打开备份文件
f_b=open("D:\Python-Project\8.12-bill.txt.bak","w",encoding="UTF-8")
# 按行读取 此时按行 for line 字符串 去掉首位空白字符 按逗号分割 将字符串切割成为列表 若列表最后一个元素是 正式 那么 写入（用追加的方式写入）备份文件中 
for line in f:
    line=line.strip()
    line_list=line.split(',')
    # if line_list[4]=="remarks" or line_list[4]=="正式":
    #     f_b.write(line)
    #     f_b.write("\n")
# 这样更好一些
    if line_list[4]=="测试":
        continue
    else:
        f_b.write(line)
        f_b.write("\n")
# 关闭两个文件
f.close()
f_b.close()