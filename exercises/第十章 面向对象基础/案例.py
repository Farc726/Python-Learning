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
        return f"姓名：{self.s_name}|语文：{self.s_chinese}|数学：{self.s_math}|英语：{self.s_english}"
    def update_s(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.s_chinese=chinese
        if math is not None:
            self.s_math=math
        if english is not None:
            self.s_english=english
            
            
              
        

class EduManangment:
    menu="""# 1．添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        # 2．修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
        # 3．删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
        # 4．查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        # 5．展示全部学生成绩：展示出系统中所有学生的成绩"""
# 教务系统中储存了大量的学生信息----其中有一个学生信息的列表meimei添加学生信息就向列表中加元素（这里的元素是什么呢？）是一个student类
    def __init__(self):
        self.student_list=[]
        
# 根据功能来决定类的内部构造
# 功能一：添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    # 1.输入学生姓名
    # 2.判断教务系统中是否已经存在该学生的信息
    # 3.若不存在 进行添加操作（继续向下输入分数）
    # 4.判断分数是否在1~100之间
    # 5.分数输入完毕 添加完成
    def add_s(self):
    #第一遍写的时候整体来收思路没有问题 细节1.循环的时候尽量不要用下标来循环     2.与c语言不同注意大于等于小于等于的写法    3.多种方法 最简洁的一种 判断完成之后可以直接return了
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
    # 1.输入学生姓名
    # 2.判断教务系统中是否已经存在该学生的信息
    # 3.若不存在 提示不存在后返回
    # 4.若存在 输入要修改的成绩 
    def change_s(self):
        name = input("请输入您要修改成绩的学生姓名：")
        for s in self.student_list:
            if name==s.s_name:
                chinese=int(input(f"请输入{name}同学的语文成绩："))
                math=int(input(f"请输入{name}同学的数学成绩："))
                english=int(input(f"请输入{name}同学的英语成绩："))
                if (0<=chinese<=100) and (0<=math<=100) and (0<=english<=100):
# 这个地方你原先写的是s = Student(name,chinese,math,english) 
# 这只是改变了循环中s的指向 并没改变原列表中储存的Student数据
# 要么用s.s_chinese=chinese修改 要么就zaiStudent中定义专门的修改函数更直观高效一点
                    s.update_s(chinese,math,english)
                else:
                     print("请输入正确的成绩数据:(0~100)")
            else:
                print("教务系统中无该学生信息~")
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




print("欢迎使用教务管理系统~~ 请按菜单要求进行操作")
e1=EduManangment()   

while True:
    e1.show_menu()
    order=input("请输入您要进行的操作：")
    
    match order:
        case "1":
            e1.add_s()
        case "2":
            e1.change_s()
        case "3":
            e1.delete_s()
        case "4":
            e1.search_s()
        case "5":
            e1.show_s()
        case _:
            break
            
    

            

        


    