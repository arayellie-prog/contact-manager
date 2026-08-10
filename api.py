from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contact_manager import ContactManager
from contact import Contact
import json
manager=ContactManager()
app=FastAPI()
templates=Jinja2Templates(directory='templates')
@app.get('/',response_class=HTMLResponse)
def home(request:Request):
    
    
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={'contacts':manager.contacts}
    )
@app.post('/contacts',response_class=HTMLResponse)
def add(request:Request,name:str=Form(),phone:int=Form()):
    manager.add_contact(name,phone)
    manager.save_contacts()

    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={'contacts':manager.contacts}
    )

@app.post('/delete',response_class=HTMLResponse)
def delete(request:Request,del_id:int=Form()):
    del_contact=manager.search_id(del_id)
    if del_contact:
        manager.del_contact(del_contact)
        manager.save_contacts()
    return templates.TemplateResponse(
            request=request,
            name='index.html',
            context={'contacts':manager.contacts}
        )

@app.get('/edit/{edit_id}',response_class=HTMLResponse)
def update(request:Request,edit_id:int):
    return templates.TemplateResponse(
                request=request,
                name='index.html',
                context={'contacts':manager.contacts,
                         'edit_id':edit_id
                         }
            )

@app.post('/update',response_class=HTMLResponse)
def update(request:Request,edit_id:int=Form(),edit_name:str=Form(),edit_phone:int=Form()):
    edit_contact=manager.search_id(edit_id)
    edit_contact.update(edit_name,edit_phone)
    manager.save_contacts()
    return templates.TemplateResponse(
                request=request,
                name='index.html',
                context={'contacts':manager.contacts}
            )
