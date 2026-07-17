from contact_manager import ContactManager
from contact import Contact
import sys

manager = ContactManager()


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
                while True:
                    name = input("请输入姓名")
                    if manager.search_name(name):
                        print("联系人已存在，请重新输入新增联系人姓名")
                    else:
                        phone = input("请输入电话")
                        contact=Contact(name,[phone])
                        manager.add_contact(contact)
                        manager.save_contacts()
                        break
            case 2:
                while True:
                    name = input("请输入姓名")
                    contact=manager.search_name(name)
                    if contact:
                        phone = input("请输入电话")
                        result=contact.add_phone(phone)
                        if result:
                            print(contact.name ,contact.phone)
                            break
                        else:
                            print("该电话已存在")

                manager.save_contacts()
            case 3:
               while True:
                   name = input("请输入姓名")
                   contact=manager.search_name(name)
                   if contact:
                       editName=input("修改后的名字：")
                       contact.edit_name(editName)
                       manager.save_contacts()
                       break
                   else:
                       print("未找到联系人")
 
            case 4:
                name = input("请输入姓名")
                contact=manager.search_name(name)
                while not contact:
                        print("未找到联系人")
                        name = input("请输入姓名")
                        contact=manager.search_name(name)
                    
                       
                while True:
                    
                    print(contact.show_phone())
                    num=input('需要修改的电话序号：')
                    if contact.lock_phone(num):
                        editPhone=input("修改后的电话：")
                        contact.edit_phone(num,editPhone)
                        manager.save_contacts()
                        break
                    else:
                        print("请输入正确下标")
                      
            case 5:
                while True:
                    name=input("请输入姓名")
                    contact=manager.search_name(name)
                    if contact:
                        manager.del_contact(contact)
                        manager.save_contacts()
                        break
                    else:
                        print("未找到联系人")
            case 6:
                 name = input("请输入姓名")
                 contact=manager.search_name(name)
                 while not contact:
                        print("未找到联系人")
                        name = input("请输入姓名")
                        contact=manager.search_name(name)
                    
                       
                 while True:
                    
                    print(contact.show_phone())
                    num=input('需要删除的电话序号：')
                    if contact.lock_phone(num):
                        contact.del_phone(num)
                        manager.save_contacts()
                        break
                    else:
                        print("请输入正确下标")
            case 7:
                manager.save_contacts()
                print("正在保存数据...正在退出...")
                manager.save_contacts()
                sys.exit()
            case _:
                print("请输入正确的数字")
    except ValueError:
        print("请输入数字")
    
 