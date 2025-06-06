from utils.controller import add_user,get_user_info, remove_user,update_user
from utils.model import users



def main():
    while True:
        print('============MENU=============')
        print('0 - zakończe program')
        print('1 - wyświetl co u znajomych')
        print('2 - dodaj znajomego')
        print('3 - usuń znajomego')
        print('4 - zauktualizuj dane znajomego')
        print('5 - Wygeneruj mapę znajomych')
        print('=============================')
        choice: str = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)
if __name__ == '__main__':
    main()