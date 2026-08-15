# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：

# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。

# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。

# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。

# 5．退出购物车

# 定义商品类
class Goods:
# 类中包含：商品信息（商品名称、价格、数量）
    def __init__(self,name,price,amount):
        self.name=name
        self.price=price
        self.amount=amount
# 题目中涉及到展示产品的信息 定义展示产品信息的方法
    def show_goods(self):
        print(f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.amount}")

# 定义管理系统类
class ShoppingCart:
# 系统要包含添加的购物车的商品信息 放在列表中列表中的元素就是前面定义的商品类
    def __init__(self):
        self.goods_list=[]
# 菜单页面输出
    def show_menu(self):
        print("----------------------------------------------------------------")
        print("1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出购物车")
        print("----------------------------------------------------------------")
# 功能一：添加购物车
    def add_goods(self):
        name=input("请输入您要添加的商品名称：")
        for s in self.goods_list:
            if s.name==name:
                print("此商品已在购物车中 请勿重复添加~")
                print("添加操作执行完毕~")
                return
        
        price=float(input("请输入您要添加的商品价格："))
        amount=int(input("请输入您要添加的商品数量："))
        if price>0 and amount>0:
            s=Goods(name,price,amount)
            self.goods_list.append(s)
        else:
            print("请输入合理的商品价格/数量")
        print("商品添加操作执行完毕~")
                
            
# 功能二：修改购物车
    def update_goods(self):
        name=input("请输入您要修改的商品名称：")
        for s in self.goods_list:
            if s.name==name:
               price=float(input("请输入您要修改的商品价格：")) 
               amount=int(input("请输入您要修改的商品数量："))
               if price>0 and amount>0:
                   s.price=price
                   s.amount=amount
                   print("商品信息修改完毕~")
               else:
                   print("请输入合理的商品价格/数量")
                   print("修改操作执行完毕~")
               return
        print("购物车中无该商品信息，请先添加")
        print("修改操作执行完毕~")
# 功能三：删除购物车
    def delete_goods(self):
        name=input("请输入您要删除的商品名称：")
        for s in self.goods_list:
            if s.name==name:
                self.goods_list.remove(s)
                print("商品信息删除完毕~")
                return
        print("购物车中无该商品信息无需删除~")
        print("删除操作执行完毕~")
            
# 功能四：查询购物车：
    def search_goods(self):
        if len(self.goods_list)==0:
            print("该购物车中无任何商品信息~")
        else:
            for s in self.goods_list:
                s.show_goods()
        print("查询操作执行完毕~")
# 运行整个程序
    def run_system(self):
        print("欢迎使用购物车管理系统")
        while True:
            self.show_menu()
            order=input("请选择您要进行的操作(1~5):")
            match order:
                case "1":
                    self.add_goods()
                case "2":
                    self.update_goods()
                case "3":
                    self.delete_goods()
                case "4":
                    self.search_goods()
                case "5":
                    print("系统已退出~欢迎下次使用~")
                    break
                case _:
                    print("请输入有效数字~")
                    
# 测试
if __name__=="__main__":
    shop_cart=ShoppingCart()
    shop_cart.run_system()