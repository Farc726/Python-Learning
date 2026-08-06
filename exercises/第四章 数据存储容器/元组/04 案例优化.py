# 根据提供的学生成绩单，完成如下需求：
# 1．计算每个学生的总分、各科平均分，然后一并输出出来。
# 2．统计各科成绩的最低分、最高分、平均分，并输出。
# 3．查找成绩优秀（平均分大于 90）的学生，并输出。

students = (
("S001","王林",85,92,78),
("S002","李磊瑜",92,88,95),
("S003","十三",78,85,82),
("S004","曾牛",88,79,91),
("S005","闻轶",95,96,89),
("S006","王卓",76,82,77),
("S007","红蝶",89,91,94),
("S008","徐立国",75,69,82),
("S009","许木",86,89,98),
("S010","通天",66,59,72)
)
# 1．计算每个学生的总分、各科平均分，然后一并输出出来---->注意保留一位小数的写法
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
#方式一：
for s in students:#s现在是元组
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.1f}")
#方式一二进行对比 关注一下元组解包的应用
#方式二：借助于元组的解包
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/len(s)
    print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")

# 2．统计各科成绩的最低分、最高分、平均分，并输出。
# s_chinese=[]
# for s in students:
#     s_chinese.append(s[2])

#用列表推导式更加简洁
s_chinese=[s[2] for s in students]

print("语文最高分为：",max(s_chinese))
print("语文最低分为：",min(s_chinese))
print("语文平均分为：",sum(s_chinese)/len(s_chinese))
#数学英语亦然

print()
# 3．查找成绩优秀（平均分大于 90）的学生，并输出。
print("成绩优秀的学生有：")
print("学号\t姓名\t平均分")
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     if avg>=90:
#         print(f"{s[0]}\t{s[1]}\t{avg:.1f}")

for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    if avg>=90:
        print(f"{id}\t{name}\t{avg:.1f}")