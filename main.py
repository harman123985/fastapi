from fastapi import FastAPI,Depends,status,Response,HTTPException
import schemas,models
from database import SessionLocal, engine
from sqlalchemy.orm  import Session
from routers import contact,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(contact.router)
app.include_router(user.router)







