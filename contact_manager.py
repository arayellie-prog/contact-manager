import json
from contact import Contact
class ContactManager:
    def __init__(self) :
        self.contacts=self.load_contacts()

    def load_contacts(self):
        contacts=[]
        try:
            with open("data.json", "r") as file:
                convert = json.load(file)
                for item in convert:
                    contact=Contact(item['name'],item['phone'])
                    contacts.append(contact)
                return contacts
        except (FileNotFoundError ,json.JSONDecodeError):
            pass
        return contacts
        

    def search_name(self,name):
        for contact in self.contacts:
            if name==contact.name:
                return contact
        return None
    
    def add_contact(self,contact):
        self.contacts.append(contact)


        
    def save_contacts(self):
        lst=[]   
        for contact in self.contacts:
            lst.append(contact.to_dict())
        with open('data.json','w')as file:
            json.dump(lst,file)
            

    def del_contact(self,contact):
        self.contacts.remove(contact)


