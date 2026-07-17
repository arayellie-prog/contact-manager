class Contact:
    def __init__(self,name,phones):
        self.name=name
        self.phone=phones or []
    def add_phone(self,addPhone):
        if addPhone in self.phone:
            return None
        else:
            self.phone.append(addPhone)
            return True
        
    def edit_name(self,editName):
        self.name=editName
        

    def edit_phone(self,num,editPhone):
            num=int(num)
            self.phone[num]=editPhone
    def del_phone(self,index):
        index=int(index)
        self.phone.pop(index)
    def to_dict(self):
        dic= {'name':self.name,'phone':self.phone}
        return dic
    def show_phone(self):
        show=[]
        for index,num in enumerate(self.phone):
             show.append(f'{index}.{num} ')
        return show
    
    def lock_phone(self,num):
         num=int(num)
         if 0<=num<len(self.phone) :
             return True
         else:
             return False
