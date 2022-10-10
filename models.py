from sqlalchemy import Column, ForeignKey,Integer,String
from database import Base
from sqlalchemy.orm import relationship


class Contact(Base):
    __tablename__ = 'Contacts'
    id = Column(Integer,primary_key=True,index=True)
    contactnum = Column(Integer)
    name=Column(String)
    country=Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creation = relationship("User", back_populates="creator")

    
class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    email=Column(String) 
    password = Column(String)
    
    creator = relationship("Contact", back_populates="creation")