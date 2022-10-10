from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm  import Session
import schemas,database,models
from hashing import Hash
get_db= database.get_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/',status_code=status.HTTP_201_CREATED )
def create(request:schemas.UserSchema,db:Session=Depends(get_db)):
    new_user= models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/id',response_model=List[schemas.UserSchemaGet],tags=['Users'])
def getall (db:Session = Depends(get_db)):
    users = db.query(models.User).all() 
    return users

