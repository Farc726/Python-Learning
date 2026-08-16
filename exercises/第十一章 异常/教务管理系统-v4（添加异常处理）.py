# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
# 1．添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2．修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
# 3．删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4．查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
# 5．展示全部学生成绩：展示出系统中所有学生的成绩
class Student:
# 属性： name chinese math English
    def __init__(self,name,chinese,math,english):
        self.s_name=name
        self.s_chinese=chinese
        self.s_math=math
        self.s_english=english
    
    def __str__(self):
        return f"姓名：{self.s_name} | 语文：{self.s_chinese} | 数学：{self.s_math} | 英语：{self.s_english}"
    def update_s(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.s_chinese=chinese
        if math is not None:
            self.s_math=math
        if english is not None:
            self.s_english=english
            
            
# 教务系统类
class EduManangment:
    version="3.0"
    menu="""
            # 1.添加学生成绩
            # 2.修改学生成绩
            # 3.删除学生成绩
            # 4.查询指定学生成绩
            # 5展示全部学生成绩
            # 6.退出系统"""

    def __init__(self):#用于初始化这个类
        self.student_list=[]
        

# 功能一：添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    def add_s(self):

        name = input("请输入您要添加的学生姓名：")
        for s in self.student_list:
            if name==s.s_name:
                print("此学生的成绩已在教务系统中~不可添加~")
                return
        
        chinese=int(input(f"请输入{name}同学的语文成绩："))
        math=int(input(f"请输入{name}同学的数学成绩："))
        english=int(input(f"请输入{name}同学的英语成绩："))
        if (0<=chinese<=100) and (0<=math<=100) and (0<=english<=100):
            stu=Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("请输入正确的成绩数据:(0~100)")
        print("添加操作执行完毕~")
        
# 2．修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    def change_s(self):
        name = input("请输入您要修改成绩的学生姓名：")
        for s in self.student_list:
            if name==s.s_name:
                chinese=int(input(f"请输入{name}同学的语文成绩："))
                math=int(input(f"请输入{name}同学的数学成绩："))
                english=int(input(f"请输入{name}同学的英语成绩："))
                if (0<=chinese<=100) and (0<=math<=100) and (0<=english<=100):

                    s.update_s(chinese,math,english)
                    print("修改操作执行完毕~")
                else:
                     print("请输入正确的成绩数据:(0~100)")
                     return
        print("教务系统中无该学生成绩")
        print("修改操作执行完毕~")
            
            

# 3．删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    def delete_s(self):
        name = input("请输入您要删除的学生姓名：")
        for s in self.student_list:
            if name==s.s_name:
                self.student_list.remove(s)
                print("删除操作执行完毕！")
                return
        print("教务系统中尚不存在该同学成绩")
        print("删除操作执行完毕！")

# 4．查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    def search_s(self):
         name = input("请输入您要查询的学生姓名：")
         for s in self.student_list:
             if name==s.s_name:
                 print(s)
                 print("查询操作执行完毕！")
                 return
         print("未查询到该同学信息~")
         print("查询操作执行完毕！")
         
# 5．展示全部学生成绩：展示出系统中所有学生的成绩
    def show_s(self):
        if len(self.student_list)==0:
            print("教务系统中无任何学生的成绩")
        else:
            for s in self.student_list:
                print(s)
        print("展示所有成绩操作执行完毕~")

    def show_menu(self):
        print(self.menu)
# 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统{self.version}~~ 请按菜单要求进行操作")
        while True:
            self.show_menu()
            order=input("请输入您要进行的操作：")
# 经分析 这一部分代码有可能出问题
            try:
                match order:
                    case "1":
                        self.add_s()
                    case "2":
                        self.change_s()
                    case "3":
                        self.delete_s()
                    case "4":
                        self.search_s()
                    case "5":
                        self.show_s()
                    case "6":
                        print("您已退出系统~")
                        break
                    case _:
                        print("请输入正确的操作编号~")
            except ValueError as e:
                print("数据类型错误，异常为：",e)
            except Exception:
                print("程序运行错误 请联系管理员进行处理~")
                    
                    
# 测试
if __name__=="__main__":
    edu_mangement=EduManangment()
    edu_mangement.run()