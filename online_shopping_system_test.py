'''
    > 请设计实现一个商城系统，商城主要提供两个功能：商品管理、会员管理。
    >
    > 商品管理：
    >
    > - 查看商品列表
    > - 根据关键字搜索指定商品
    > - 录入商品
    >
    > 会员管理：【无需开发，如选择则提示此功能不可用，正在开发中，让用户重新选择】

    需求细节：

    1. 启动程序让用户选择进行商品管理 或 会员管理，如：
       ![输入图片说明](https://images.gitee.com/uploads/images/2019/0412/171126_0567693f_73459.png "屏幕截图.png")
    2. 用户选择 【1】 则进入商品管理页面，进入之后显示商品管理相关的菜单，如：
       ![输入图片说明](https://images.gitee.com/uploads/images/2019/0412/171201_47d7aa64_73459.png "屏幕截图.png")
    3. 用户选择【2】则提示此功能不可用，正在开发中，让用户重新选择。
    4. 如果用户在【商品管理】中选择【1】，则按照分页去文件 goods.txt 中读取所有商品，并全部显示出来【分页功能可选】。
    5. 如果用户在【商品管理】中选择【2】，则让提示让用户输入关键字，输入关键字后根据商品名称进行模糊匹配，如：
       ![输入图片说明](https://images.gitee.com/uploads/images/2019/0412/171227_049ea3f5_73459.png "屏幕截图.png")
    6. 如果用户在【商品管理】中选择【3】，则提示让用户输入商品名称、价格、数量 然后写入到 goods.txt 文件，如：
       ![输入图片说明](https://images.gitee.com/uploads/images/2019/0412/171251_b1080b58_73459.png "屏幕截图.png")
'''
def membership_management():
    print('功能不可用，正在开发中，请重新选择')


def goods_management(numb):
    '''查看商品列表
    根据关键字搜索指定商品
    录入商品'''
    if numb == '1': # 查看商品列表
        goods_list = open('goods.txt',mode='r',encoding='utf-8').read()
        print(goods_list)
   
    if numb == '2': # 根据关键字搜索指定商品
        target = input('请输入关键字：').strip()
        goods_list = open('goods.txt',mode='r',encoding='utf-8').readlines()
        got = False
        for item in goods_list:
            if target in item:
                print(item)
                got = True
        if got == False:
            print('未找到指定物品')

    if numb == '3': # 录入商品
        while True:
            name = input('请输入商品名称（输入N返回上一级）：').strip()
            if name == 'N' or name == 'n':
                break
            price = input('请输入商品价格：').strip()
            amount = input('请输入商品数量：').strip()
            goods_list = open('goods.txt','a+',encoding='utf-8')
            goods_list.write(f'\n{name} {price} {amount}')
            print('添加成功')
      

while True:
    print('******欢迎使用老子的购物商城******\n1.商品管理\n2.会员管理\n')
    a = input('请选择（输入N返回上一级）：').strip()
    if a == 'n' or a == 'N':
            break
    elif a == '1':
        while True:
            print('******欢迎使用老子的购物商城[商品管理]******\n1.查看商品列表\n2.根据关键字搜索指定商品\n3.录入商品\n')
            b = input('请选择（输入N返回上一级）').strip()
            if b == 'N' or b == 'n':
                break
            goods_management(b)
    elif a == '2':
        membership_management()
    else:
        print('输入错误，请重新输入！')