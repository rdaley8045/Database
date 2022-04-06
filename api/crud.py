from sqlalchemy.orm import Session
import model
from tables import Roster, Squadron, Grade


def getIndividualsInSquadron(db: Session, squadronName: str):
    return db.query(Roster.callsign, Roster.commander, Roster.executive, Grade.position).join(Squadron, Grade).\
        filter(Squadron.name == squadronName).all()


# def create_user(db: Session, user: model.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
