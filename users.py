import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class UserDB(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
class UserRegister():
    def __init__(self, db_path, userData): # В конструкторе получем введенные данные нового пользователя
        self.db_path = db_path
        self.userData = userData
        self.first_name = self.userData[0]
        self.last_name = self.userData[1]
        self.gender = self.userData[2]
        self.email = self.userData[3]
        self.birthdate = self.userData[4]
        self.height = self.userData[5]
    def addUserToDB(self): # Метод для добавления данных нового пользователя в БД
        self.engine = sa.create_engine(self.db_path)
        self.Sessions = sessionmaker(self.engine)
        self.session = self.Sessions()
        self.newUser = UserDB(first_name = self.first_name, last_name = self.last_name, gender = self.gender, email = self.email, birthdate = self.birthdate, height = self.height)
        self.session.add(self.newUser)
        self.session.commit()

         

