from users import UserRegister
from find_athlete import DBMethods
DB_PATH = "sqlite:///sochi_athletes.sqlite3"

def enterUserData():
    first_name = input('Enter user Name:')
    last_name = input('Enter last name:')
    gender = input('Enter gender:')
    email = input('Enter email:')
    birthdate = input('Enter birthday:')
    height = input('Enter height:')
    userData = [first_name,last_name,gender,email,birthdate,height]
    return userData 

def main():
    print('What do you want to do?\nType 1, 2, 3 or 4\n1 - add new user\n2 - find most close user by user`s id to athlet from athlet`s db\n3 - show user`s db\n4-delete record by id\n5- quit')
    choose = input()
    if choose == '1':
        newUserData = enterUserData() # Вводим данные нового пользователя
        regNewUser = UserRegister(DB_PATH, newUserData) # Регистрируем нового пользователя в БД
        regNewUser.addUserToDB()
        print('User {} {} registered..'.format(newUserData[0], newUserData[1]))
    elif choose == '2':
        findRecord = DBMethods(DB_PATH)
        id = int(input('Enter id: '))
        if findRecord.isUserInDB(id):
            pass
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
        #break
    else:
        print('Wrong input! Try one more time')

    # while True:
        # newUser = UserRegister(DB_PATH)
        # print('What do you want to do?\nType 1, 2, 3 or 4\n1 - add new user\n2 - find most close user by user`s id to athlet from athlet`s db\n3 - show user`s db\n4- quit')
        # choose = input()
        # if int(choose) == 1:
        #     newUser.addUser()
        # elif int(choose) == 2:
        #     print('Finding athlet..')
        # elif int(choose) == 3:
        #     newUser.showDB()
        # elif int(choose) == 4:
        #     print('See you..')
        #     break
        # else:
        #     print('Wrong input! Try one more time')
if __name__ == "__main__":
    main()
