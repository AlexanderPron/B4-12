from users import UserRegister
from find_athlete import *
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
def main():
    while True:
        newUser = UserRegister(DB_PATH)
        print('What do you want to do?\nType 1, 2, 3 or 4\n1 - add new user\n2 - find most close user by user`s id to athlet from athlet`s db\n3 - show user`s db\n4- quit')
        choose = input()
        if int(choose) == 1:
            newUser.addUser()
        elif int(choose) == 2:
            print('Finding athlet..')
        elif int(choose) == 3:
            newUser.showDB()
        elif int(choose) == 4:
            print('See you..')
            break
        else:
            print('Wrong input! Try one more time')
if __name__ == "__main__":
    main()
