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
                    contact=Contact(item['id'],item['name'],item['phone'])
                    contacts.append(contact)
                
                return contacts
        except (FileNotFoundError ,json.JSONDecodeError):
            pass
        return contacts
        

    def search_id(self,id):
        for contact in self.contacts:
            if id==contact.id:
                return contact
        return None
    
    def get_max_id(self):
        if self.contacts:
            return max(contact.id for contact in self.contacts)
        else:
            return 0
    def add_contact(self,name,phone):
        max_id=self.get_max_id()
        id=max_id+1
        new_contact=Contact(id,name,phone)
        self.contacts.append(new_contact)
        

        
    def save_contacts(self):
        lst=[]   
        for contact in self.contacts:
            lst.append(contact.to_dict())
        with open('data.json','w')as file:
            json.dump(lst,file)
            

    def del_contact(self,contact):
        self.contacts.remove(contact)

   


