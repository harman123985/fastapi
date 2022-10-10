from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database,models
from sqlalchemy.orm import Session
from . import token

router = APIRouter(
    tags=['Authentication'])

@router.post('/login')
def login(request:schemas.login,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'datail no found')        

    access_token = token.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}