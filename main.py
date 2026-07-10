import contact_manager
while True:
    print("***Welcome to your own contact!***")
    print("----------------------------------")
    print(
    "1.新增联系人\n2.添加已有联系人电话\n3.修改联系人姓名\n4.修改联系人电话\n5.删除联系人\n6.删除联系人电话\n7.退出程序"
)
    try:
        button = int(input("你要做什么？请输入对应数字"))
        match button:
            case 1:
                contact_manager.add_contact()
            case 2:
                contact_manager.add_phone()
            case 3:
                contact_manager.edit_name()
            case 4:
                contact_manager.edit_phone()
            case 5:
                contact_manager.del_contact()
            case 6:
                contact_manager.del_phone()
            case 7:
                contact_manager.save()
            case _:
                print("请输入正确的数字")
    except ValueError:
        print("请输入数字")
