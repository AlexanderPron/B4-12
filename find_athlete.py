import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date, time
import time
Base = declarative_base()
class UserDB(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    # birthdate = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.DATE)
    height = sa.Column(sa.REAL)
class AtheleteDB(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    # birthdate = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.DATE)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)
    
class DBMethods():
    def __init__(self, db_path):
        self.db_path = db_path
        self.engine = sa.create_engine(self.db_path)
        self.Sessions = sessionmaker(self.engine)
        self.session = self.Sessions()

    def showUserDB(self):
        self.records = self.session.query(UserDB).all()
        return self.records

    def isUserInDB(self, id): # Метод для проверки наличия пользователя с заданным id в БД
        self.id = id
        self.user_ids = [self.user.id for self.user in self.session.query(UserDB).all()]
        if self.id in self.user_ids:
            return True
        else:
            return False

    def delRecordById(self, id): # Метод для удаления пользователя по id записи (пока только по 1 юзеру) TODO Удалять список юзеров
        self.id = id
        self.session.query(UserDB).filter_by(id=self.id).delete()
        self.session.commit()

    def findCloseAthelets(self, id):
        self.id = id
        self.userRecord = self.session.query(UserDB).filter_by(id=self.id).first()
        self.userBirthday = self.userRecord.birthdate
        self.userHeight = self.userRecord.height
        # select * from athelete where height > 0 order by abs(150-height*100) limit 1;
        self.closeByHeightAthelete = self.session.query(AtheleteDB).filter(AtheleteDB.height > 0).order_by(sa.func.abs(AtheleteDB.height*100 - self.userHeight)).first()
        self.closeByBirthdayAthelete = self.session.query(AtheleteDB).order_by(sa.func.abs(AtheleteDB.birthdate - self.userBirthday)).first()
        print('{}:{}'.format(self.closeByBirthdayAthelete.id, self.closeByBirthdayAthelete.birthdate))


        
