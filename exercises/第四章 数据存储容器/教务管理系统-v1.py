# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5．列出所有学生：遍历所有学生信息并输出。
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7．退出系统。

# 现在是s={name:{"chinese":chinese,"math":math,"English",English}}   6到底怎么做不问AI明天自己好好想一下！！
print("欢迎使用教务管理系统~")
s={}
menu="""#############################【菜单】#############################
# 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统   #
################################################################"""

while True:
    print(menu)
    order=input("请选择您将要执行的操作(1~7):")
    match order:
        case "1":
            name=input("请输入要录入的学生的姓名：")
            if name in s:
                print("该学生信息已在系统中，无需再次录入~")
            else:
                chinese=float(input("请录入其语文成绩："))
                math=float(input("请录入其数学成绩："))
                English=float(input("请录入其英语成绩："))
                s[name]={"chinese":chinese,"math":math,"English":English}
                print("该同学的成绩录入成功！")

        case "2":
            name=input("请输入要修改的学生的姓名：")
            if name not in s:
                print("该学生信息不在系统中，请先录入~")
            else:
                s[name]["chinese"]=float(input("请录入其修改后的语文成绩："))
                s[name]["math"]=float(input("请录入其修改后的数学成绩："))
                s[name]["English"]=float(input("请录入其修改后的英语成绩："))
                print("该同学的成绩修改成功！")

        case "3":
            name=input("请输入要删除的学生的姓名：")
            if name not in s:
                print("系统中不存在该同学的信息无需删除~")
            else:
                del s[name]
                print(f"{name}同学的信息删除成功~")
        case "4":
            name=input("请输入要查询的学生的姓名：")
            if name not in s:
                        print("该学生信息不在系统中")
            else:
                print("姓名\t语文\t数学\t英语")
                print(f"{name}\t{s[name]['chinese']}\t{s[name]['math']}\t{s[name]['English']}\t")
        case "5":
            if len(s)==0:
                print("系统中没有任何一位同学的信息")
            else:
                print("姓名\t语文\t数学\t英语")
                for name in s:
                    print(f"{name}\t{s[name]['chinese']}\t{s[name]['math']}\t{s[name]['English']}\t")
        case "6":# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
            if(len(s)==0):
                print("系统中没有任何一位同学的信息")
            else:
                s_chinese=[]
                s_math=[]
                s_English=[]
                for name in s:
                    s_chinese.append(s[name]["chinese"])
                    s_math.append(s[name]["math"])
                    s_English.append(s[name]["English"])
#平均分保留2位小数 防止输出一长串
                print(f"语文最高分为：{max(s_chinese)},平均分为:{sum(s_chinese)/len(s_chinese):.2f}")
                print(f"数学最高分为：{max(s_math)},平均分为:{sum(s_math)/len(s_math):.2f}")
                print(f"英语最高分为：{max(s_English)},平均分为:{sum(s_English)/len(s_English):.2f}")
                
                # for name in s:
                #     if s[name]["chinese"]==max(s_chinese):
                #         c_max=name
                #     if s[name]["chinese"]==min(s_chinese):
                #         c_min=name
                #     if s[name]["math"]==max(s_math):
                #         m_max=name
                #     if s[name]["math"]==min(s_math):
                #         m_min=name
                #     if s[name]["English"]==max(s_English):
                #         e_max=name
                #     if s[name]["English"]==min(s_English):
                #         e_min=name
#修改 若出现多人并列的情况;
                c_max=[]
                c_min=[]
                m_max=[]
                m_min=[]
                e_max=[]
                e_min=[]
                
                for name in s:
                    if s[name]["chinese"]==max(s_chinese):
                        c_max.append(name)
                    if s[name]["chinese"]==min(s_chinese):
                        c_min.append(name)
                    if s[name]["math"]==max(s_math):
                        m_max.append(name)
                    if s[name]["math"]==min(s_math):
                        m_min.append(name)
                    if s[name]["English"]==max(s_English):
                        e_max.append(name)
                    if s[name]["English"]==min(s_English):
                        e_min.append(name)
                
# 注意:打印格式 问了AI------"连接符".join(序列)---join不接受 int/float
                print(f"取得语文最高分的同学为：{'、'.join(c_max)}")
                print(f"取得语文最低分的同学为：{'、'.join(c_min)}")
                print(f"取得数学最高分的同学为：{'、'.join(m_max)}")
                print(f"取得数学最低分的同学为：{'、'.join(m_max)}")
                print(f"取得英语最高分的同学为：{'、'.join(e_max)}")
                print(f"取得英语最低分的同学为：{'、'.join(e_max)}")
                
                
                
        case "7":
            print("感谢使用~ 成功退出系统~")
            break
        case _:
            print("请输入正确的数字~")
        