class Contact:
    def __init__(self,id,name,phones):
        self.id=id
        self.name=name
        self.phone=phones 
    def add_phone(self,addPhone):
        if addPhone in self.phone:
            return None
        else:
            self.phone.append(addPhone)
            return True
        
  
        
    def update(self,edit_name,edit_phone):
        self.name=edit_name
        self.phone=edit_phone
   
    
    def to_dict(self):
        dic= {'id':self.id,'name':self.name,'phone':self.phone}
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
