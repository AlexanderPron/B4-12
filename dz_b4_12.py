from users import UserRegister
from find_athlete import DBMethods
from datetime import datetime, date, time
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
GENDER = ['male','female']

def isCorrectDate(enteredDate): # Функция проверки корректности введенной даты рождения
    try:
        datetime.strptime(enteredDate, "%Y-%m-%d") # Вылетит ошибка, если проверяемая дата указана не по шаблону. 
        return True
    except Exception:
        return False
def birthdateToTimestamp(data):
    ts=datetime.strptime(data, "%Y-%m-%d").timestamp()
    return ts



def isCorrectEmail(email):
    """
    Проверяет наличие хотя бы одной точки в домене и одного знака @ в email. Возвращает True, если email допустимый, и False — в противном случае.
    """
    if email.find("@") >= 1 and email.count("@") == 1 and email.rfind(".") > email.find("@"):
        return True
    else:
        return False

def enterUserData():
    first_name = input('Enter user Name:')
    last_name = input('Enter last name:')
    gender = input('Enter gender (male/female):')
    while True:
        email = input('Enter email:')
        if isCorrectEmail(email):
            break
        else:
            print('Wrong email! Try one more time..')
    while True:
        birthdate = input('Enter birthday (CORRECT FORMAT YYYY-MM-DD) :')
        if isCorrectDate(birthdate):
            break
        else:
            print('Wrong date! Try one more time..')
    height = input('Enter height (sm):')
    userData = [first_name,last_name,gender,email,birthdate,height]
    return userData 

def main():
    
    while True:
        print('What do you want to do?\nType 1, 2, 3, 4 or 5\n1 - add new user\n2 - find most close user by user`s id to athlet from athlet`s db\n3 - show user`s db\n4 - delete record by id\n5 - quit')
        choose = input('-> ')
        if choose == '1':
            newUserData = enterUserData() # Вводим данные нового пользователя
            regNewUser = UserRegister(DB_PATH, newUserData) # Регистрируем нового пользователя в БД
            regNewUser.addUserToDB()
            print('User {} {} registered..'.format(newUserData[0], newUserData[1]))
        elif choose == '2':
            findRecord = DBMethods(DB_PATH)
            id = int(input('Enter id: '))
            if findRecord.isUserInDB(id):
                findRecord.findCloseAthelets(id)
            else:
                print('No Record with id {}..'.format(id))
        elif choose == '3':
            newMethod = DBMethods(DB_PATH)
            records = newMethod.showUserDB()
            for item in records:
                print('{}|{}|{}|{}|{}|{}|{}'.format(item.id,item.first_name,item.last_name,item.gender, item.email, item.birthdate, item.height))
        elif choose == '4':
            delRecord = DBMethods(DB_PATH)
            id = int(input('Enter id: '))
            if delRecord.isUserInDB(id):
                delRecord.delRecordById(id)
                print('Record with id {} has been deleted..'.format(id))
            else:
                print('No Record with id {}..'.format(id))
        elif choose == '5':
            print('See you..')
            break
        else:
            print('Wrong input! Try one more time..')

if __name__ == "__main__":
    main()
