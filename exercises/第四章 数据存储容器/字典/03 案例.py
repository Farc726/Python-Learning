# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4．查询购物车（单个）：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 查询购物车（全部）：将购物车中全部商品的信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 6．退出购物车
print("欢迎使用购物车管理系统~")
menu="""########## 购物车系统 ##########
#        1. 添加购物车          #
#        2. 修改购物车          #
#        3. 删除购物车          #
#        4. 查询购物车(单个商品) #
#        5. 查询购物车(全部商品) #
#        6. 退出购物车          #
################################"""
shopcar={}

while True:
    print(menu)
    order= input("请输入您要进行的操作(1~6):")
    match order:
        case "1":
            name=input("请输入您要添加的商品名称：")
            if name in shopcar:
                print("此商品已在您的购物车内，无需添加~")
            else:
#关键！！ 这是你卡住的地方 内嵌的字典你要先让编译器知道有内嵌字典的存在！
# 注意 数据类型的转换
                prize=float(input("请输入您要添加的商品价格："))
                num=int(input("请输入您要添加的商品数量："))
                shopcar[name]={"prize":prize,"num":num}
                print("商品添加成功~")
        case "2":
            name=input("请输入您要修改的商品的名称：")
            if name not in shopcar:
                print("此商品并未在您的购物车内，请添加~")
            else:
                shopcar[name]["prize"]=float(input("请输入您要修改的商品价格："))
                shopcar[name]["num"]=int(input("请输入您要修改的商品数量："))
                print("恭喜您！修改成功！")

        case "3":
            name=input("请输入您要删除的商品名称：")
            if name not in shopcar:
                print("此商品并未在您的购物车内无需删除")
            else:
                del shopcar[name]
                print("恭喜您！删除成功！")
        case "4":
            name=input("请输入您要查询的商品名称：")
            if name not in shopcar:
                print("此商品并不在您的购物车中~")
            else:
                print(f"商品名称:{name}，商品价格:{shopcar[name]['prize']}，商品数量:{shopcar[name]['num']}")
        case "5":
            if len(shopcar)==0:
                print("您的购物车中没有任何物品")
            else:
                print("您购物车中所有的商品信息如下：")
                for name in shopcar:
                    print(f"商品名称:{name}，商品价格:{shopcar[name]['prize']}，商品数量:{shopcar[name]['num']}")
       
        case "6":
            print("操作完成！已退出~")
            break
        case _:
            print("请输入有效数字~")

