from typing import List
from fastapi import APIRouter,Depends,status,Response
from sqlalchemy.orm  import Session
import schemas,database,models
get_db= database.get_db

router = APIRouter(
    prefix='/contact',
    tags=['Contacts']
)

@router.get('',response_model=List[schemas.ContactSchemaGet])
def all (db:Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()
    return contacts

@router.post('',status_code=status.HTTP_201_CREATED)
def create (User_Id:int,request : schemas.ContactSchema,db:Session = Depends(get_db)):
    new_contact= models.Contact(name=request.name,country=request.country,contactnum=request.contactnum,user_id = User_Id)
    User = db.query(models.User).filter(models.User.id==User_Id).first()
    if not User:
        return {'user':'not found'}
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact 

@router.get('/id',response_model=schemas.ContactSchema)
def get_one (Id:int,response:Response,db:Session = Depends(get_db)):
    contacts = db.query(models.Contact).filter(models.Contact.id==Id).first()
    if not contacts:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'datail':'no found'}
    db.commit()
    return contacts

@router.put('')
def update(Id:int,response:Response,request : schemas.ContactSchema,db:Session = Depends(get_db)):
    contacts = db.query(models.Contact).filter(models.Contact.id==Id).first()
    if not contacts:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':'not found'}
    contacts.name=request.name
    contacts.country=request.country
    contacts.contactnum=request.contactnum
    
    db.commit()
    return {"Updated"}

@router.delete('')
def delete (Id:int,response:Response,db:Session = Depends(get_db)):
    contacts = db.query(models.Contact).filter(models.Contact.id==Id).first()
    if not contacts:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':'not found'}
    db.delete(contacts)
    db.commit()
    return {'deleted succesfully'}