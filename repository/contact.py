from sqlalchemy.orm import Session
from .. import models

def get_all(db:Session):
    contacts = db.query(models.Contact).all()
    return contacts