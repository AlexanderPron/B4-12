import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
class UserRegister():
    def __init__(self, db_path): # В конструкторе будем создавать соединение с базой данных (далее БД)
        self.db_path = db_path
        self.engine = sa.create_engine(self.db_path)
        self.Sessions = sessionmaker(self.engine)
        self.session = self.Sessions()
    def addUser(self): # Метод для добавления данных нового пользователя в БД
        self.first_name = input('Enter user Name:')
        self.last_name = input('Enter last name:')
        self.gender = input('Enter gender:')
        self.email = input('Enter email:')
        self.birthdate = input('Enter birthday:')
        self.height = input('Enter height:')
        self.newUser = User(first_name = self.first_name, last_name = self.last_name, gender = self.gender, email = self.email, birthdate = self.birthdate, height = self.height)
        self.session.add(self.newUser)
        self.session.commit()
        print('User {} {} added..'.format(self.first_name, self.last_name))
    def showDB(self):
        self.query = self.session.query(User).all()
        for item in self.query:
            print('{}|{}|{}|{}|{}|{}|{}'.format(item.id,item.first_name,item.last_name,item.gender, item.email, item.birthdate, item.height))

    def isUserInDB(self, id): # Метод для проверки наличия такого пользователя в БД
        self.id = id
         

