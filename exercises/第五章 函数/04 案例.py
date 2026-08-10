# 1．定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。

# 2．定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。

# 3．定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。

#2.
#自己写的 并不最佳
# def count_y(s):
#     """本函数用于计算字符串中元音字母的个数（大小写都算）
#     其中传入的s为要计算的字符串
#     返回值即为该字符串中元音字母的个数
#     """
    
#     a_number=s.lower().count("a")
#     e_number=s.lower().count("e")
#     i_number=s.lower().count("i")
#     o_number=s.lower().count("o")
#     u_number=s.lower().count("u")
    
#     number=a_number+e_number+i_number+o_number+u_number
#     return number

#另一种---用in 更简洁也更好
def count_y(s):
    """本函数用于计算字符串中元音字母的个数（大小写都算）
    其中传入的s为要计算的字符串
    返回值即为该字符串中元音字母的个数
    """
    number=0
    for i in s:
        if i in "aeiouAEIOU":
            number+=1
    return number

s=input("请输入您要计算的字符串：")
number=count_y(s)
print(f"其中元音字母的个数为{number}")
#反思：自己想到了查找字符串中的特定字母可以用count 但是在过程中字符串你遍历了5遍效率极低！
# 以后再判断某字符是否在特定字符串中时 用in！！！！！ 在考虑所谓“字符”怎么拿取呢 --- 用for循环来遍历 这样的话只用遍历一遍字符串

# 3．定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(l):
    """该函数用于计算传入学生成绩列表中的最高分，最低分，平均分"""
    return max(l),min(l),round(sum(l)/len(l),1)
l=[99,87,62,77,65]
s_max,s_min,s_avg=calc_score(l)
print(f"最高分为：{s_max:.1f}")
print(f"最低分为：{s_min:.1f}")
print(f"平均分为：{s_avg}")
## 写这个案例的时候  你又学到了：
# round(n,1) 数据四舍五入 原始数值被修改
# f"{n:.1f}" 也会四舍五入 不过 只是格式化打印 原始数据完全不变

# 晚上可以回去优化你的教务管理系统了~
