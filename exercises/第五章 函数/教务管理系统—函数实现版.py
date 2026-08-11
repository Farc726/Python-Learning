# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5．列出所有学生：遍历所有学生信息并输出。
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7．退出系统。



print("欢迎使用教务管理系统~~")
menu="""#############################【菜单】#############################
# 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统   #
################################################################"""
def show_menu():
    """该函数用于菜单的输出 提示用户操作"""
    print(menu)

#由题意 学生信息靠学生姓名索引 所以考虑用字典存储学生信息
infor_s={}
#大致结构为{name:{"chinese":chinese,"math":math,"English":English}}


# 核心功能实现函数的编写
# 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
def add_s():
#输入学生姓名-作为外层字典的键
    name=input("请输入要录入的学生姓名：")
#判断是否重复
    if name in infor_s:
        print("教务系统中已有此学生信息，请勿重复添加~")
    else:#如不重复-完善内层分数字典
        #明确外层字典的值也是一个字典
        infor_s[name]={}
        chinese=int(input("请输入该学生的语文成绩："))
        math=int(input("请输入该学生的数学成绩："))
        English=int(input("请输入该学生的英语成绩："))
        infor_s[name]["chinese"]=chinese
        infor_s[name]["math"]=math
        infor_s[name]["English"]=English
    print("添加操作执行完毕~")
    
# 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
def change_s():
#输入姓名
    name=input("请输入要修改的学生姓名：")
#判断存在
    if name not in infor_s:
        print("系统中无该学生信息 请先进行添加~")
    else:#改
        infor_s[name]["chinese"]=int(input("请输入修改后的语文成绩："))
        infor_s[name]["math"]=int(input("请输入修改后的数学成绩："))
        infor_s[name]["English"]=int(input("请输入修改后的英语成绩："))
    print("成绩修改工作执行完毕~")
    
# 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
def del_s():
#输入姓名
    name=input("请输入要删除的学生姓名：")
#判断存在
    if name not in infor_s:
        print("系统中无该学生信息 无需删除~")
    else:
        del infor_s[name]
    print("学生信息删除工作执行完毕~")

# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
def search_s():
    name=input("请输入要查询的学生姓名：")
    if name not in infor_s:
        print("系统中无该学生信息")
    else:
        print("姓名\t语文\t数学\t英语")
        print(f"{name}\t{infor_s[name]['chinese']}\t{infor_s[name]['math']}\t{infor_s[name]['English']}")
    print("成绩查询操作执行完毕~")
    
# 5．列出所有学生：遍历所有学生信息并输出。
def all_s():
    if len(infor_s)==0:
        print("该系统中无任何学生信息")
    else:
        print("姓名\t语文\t数学\t英语")
        for name in infor_s:
            print(f"{name}\t{infor_s[name]['chinese']}\t{infor_s[name]['math']}\t{infor_s[name]['English']}")
    print("信息输出工作执行完毕~")
    
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 功能6的辅助函数 获得某一科的最高分、最低分、平均分
def get_subject_stat(s,sub_key):
    """
    对任意一科做统计
    :param s: 学生总字典 {姓名:{"chinese":xx,...}}
    :param sub_key: 科目字符串，可选 "chinese" / "math" / "English"
    :return: 元组 (最高分,最低分,平均分,最高分名单列表,最低分名单列表)
    """
# 我需要各科成绩的列表 这个要纯净 因为我要计算最值与平均值
# 题目还要去与姓名匹配 那可以再有一个姓名与分数在一起的
    score_list=[]# 存放该科所有分数
    name_score={}# 存放姓名与分数的字典
    for name,zidian in s.items():#s.items()将字典s的键和值打包成元组（键，值）在此处为（姓名，{科目：分数，科目：分数}）   同时注意如何接收
        score=zidian[sub_key]
        score_list.append(score)
        name_score[name]=score
    # 单科分数已经全部拿到 现计算最值
    max_val=max(score_list)
    min_val=min(score_list)
    avg_val=round(sum(score_list)/len(score_list),1)
    #用列表推导式 返回取得最值的成员名单-----在此处你有一点经验了 就是当你想要的某个新列表的元素来源于某个旧的数据容器时 可以用 ！列表推导式！简洁易读
    max_names=[name for name in name_score if max_val==name_score[name]]
    min_names=[name for name in name_score if min_val==name_score[name]]
    
    #返回最高分 最低分 平均分 取得最值的成员姓名
    return max_val,min_val,avg_val,max_names,min_names
#功能6 的 辅助函数 输出
def print_infor(t,subject):
    """该函数用于输出各科成绩的最高分 最低分 平均分 取得最高分的同学 取得最低分的同学"""
    print(f"{subject}:最高分{t[0]} 最低分{t[1]} 平均分{t[2]} 取得最高分的同学{'、'.join(t[3])} 取得最低分的同学{'、'.join(t[4])}")
#功能6 主函数
def calc_s():
    if len(infor_s)==0:
        print("该系统中无任何学生信息")
    else:
        #接收函数返回的元组
        chinese_infor=get_subject_stat(infor_s,"chinese")
        math_infor=get_subject_stat(infor_s,"math")
        English_infor=get_subject_stat(infor_s,"English")
        #打印输出
        print_infor(chinese_infor,"语文")
        print_infor(math_infor,"数学")
        print_infor(English_infor,"英语")
        

        
        

        
        
    
# def calc_s():
#     if len(infor_s)==0:
#         print("该系统中无任何学生信息")
#     else:
#         chinese_s=[infor_s[name]["chinese"] for name in infor_s]
#         math_s=[infor_s[name]["math"] for name in infor_s]
#         English_s=[infor_s[name]["English"] for name in infor_s]
#         #计算单科成绩最值
#         max_c=max(chinese_s)
#         min_c=min(chinese_s)
#         max_m=max(math_s)
#         min_m=min(math_s)
#         max_e=max(English_s)
#         min_e=min(English_s)
        
#         print(f"语文最高分为：{max_c},平均分为:{sum(chinese_s)/len(chinese_s):.2f}")
#         print(f"数学最高分为：{max_m},平均分为:{sum(math_s)/len(math_s):.2f}")
#         print(f"英语最高分为：{max_e},平均分为:{sum(English_s)/len(English_s):.2f}")
#         #寻找得到最值同学的姓名 注意并列的情况
#         #可不可以把成绩最值做成一个字典 之后 键是成绩的最值 之后 值是列表类型 列表里面是取得最值的学生姓名{100：["Jack","Mary"]}
#         c_max=[]
#         c_min=[]
#         m_max=[]
#         m_min=[]
#         e_max=[]
#         e_min=[]
        
#         for name in infor_s:
#             if infor_s[name]["chinese"]==max_c:
#                 c_max.append(name)
#             if infor_s[name]["chinese"]==min_c:
#                 c_min.append(name)
#             if infor_s[name]["math"]==max_m:
#                 m_max.append(name)
#             if infor_s[name]["math"]==min_m:
#                 m_min.append(name)
#             if infor_s[name]["English"]==max_e:
#                 e_max.append(name)
#             if infor_s[name]["English"]==min_e:
#                 e_min.append(name)
#         print(f"取得语文最高分的同学为：{','.join(c_max)}")
#         print(f"取得语文最低分的同学为：{','.join(c_min)}")
#         print(f"取得数学最高分的同学为：{','.join(m_max)}")
#         print(f"取得数学最低分的同学为：{','.join(m_min)}")
#         print(f"取得英语最高分的同学为：{','.join(e_max)}")
#         print(f"取得英语最低分的同学为：{','.join(e_min)}")




#1.写出整体框架 (靠循环控制输入输出 ==7 -->跳出循环)  (用match case 表选项)
while True:
    show_menu()

    order=input("请输入您要进行的操作：")
    match order:
        case "1":
            add_s()
        case "2":
            change_s()
        case "3":
            del_s()
        case "4":
            search_s()
        case "5":
            all_s()
        case "6":
            calc_s()
        case "7":
            print("谢谢使用！ 已退出系统~")
            break
        case _:
            print("请输入合法的数字编号~")


        
                
        
        

    

        

        

             
