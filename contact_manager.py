import json

with open("data.json", "r") as file:
    contacts = json.load(file)


def save_contacts():
    with open("data.json", "w") as file:
        json.dump(contacts, file)


def add_contact():
    while True:
        exist = True
        add_contact_name = input("请输入你要添加的联系人姓名")
        for item in contacts:
            if item["name"] == add_contact_name:
                print("该联系人已存在")
                exist = False
        if exist:
            add_contact_phone = input("请输入她的联系方式")
            contacts.append({"name": add_contact_name, "phone": [add_contact_phone]})
            save_contacts()
            print(f"已成功添加{add_contact_name}!")
            break


def add_phone():
    while True:
        add_phone_name = input("请输入新增电话的联系人姓名")
        exist = True
        for item in contacts:
            if add_phone_name == item["name"]:
                add_phoneNum = input("请输入要添加的电话")
                item["phone"].append(add_phoneNum)
                print(f"已成功添加{add_phoneNum}到{add_phone_name}!")
                save_contacts()
                exist = False
                break
        if exist:
            print("未找到该联系人")
        else:
            break



def edit_name():
    while True:
        editName=input("请输入要修改姓名的联系人")
        exist=True
        for item in contacts:
            if editName==item['name']:
                newName=input("请输入修改后的名字")
                item['name']=newName
                print(f'修改成功：{item}')
                exist=False
                save_contacts()
                return
        if exist:
            print("没有找到该联系人")

        
            
            


def edit_phone():
    while True:
        ephoneName=input("请输入修改电话的联系人姓名")
        exist=True
        for item in contacts:
            if ephoneName==item['name']:
                print(item)
                editphone=input('请输入修改后的电话')
                item['phone']=[editphone]
                print(f"修改成功：{item}")
                exist=False
                save_contacts()
                return
        if exist:
            print("没找到该联系人")

            
                


def del_contact():
    while True:
        del_name=input("请输入需要删除的联系人姓名")
        exist=True
        for item in contacts:
            if del_name==item['name']:
                contacts.remove(item)
                save_contacts()
                print(f"已成功删除{del_name}!")
                exist=False
                break
        if exist:
            print("未找到该联系人")
        else:
            break




def del_phone():
    while True:
        del_phone_name=input("请输入删除电话的联系人姓名")
        exist=True
        for item in contacts:
            if del_phone_name==item['name']:
                print(item)
                exist=False
                while True:
                    del_phoneNum=input("请输入要删除的电话")
                    if del_phoneNum in item['phone']:
                        item['phone'].remove(del_phoneNum)
                        print(f'删除成功，当前通讯录已更新：{item}!')
                        save_contacts()
                        return
                    else:
                        print("无法找到对应电话")
        if exist:
            print("无法找到对应联系人")
        else:
            break

            
                
                    




def save():
    save_contacts()
    print("正在保存数据...保存成功！")
    exit()
