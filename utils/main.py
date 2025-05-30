from utils.controller import add_user,get_user_info, remove_user,update_user
from utils.model import users



def main():
    get_user_info(users)
    print(f"Witaj {users[0]["name"]}")
    print("=====menu=====")
    print("0 - zakończ program")
    print("1 - pokaż co u znajomych ")
    print("2 - dodaj nowego znajomego ")
    print("3-usun znajomego  ")
    print("4-zaktualizuj dane znajomego ")

    while True:
        choice : str = input("wybierz opcje MENU: ")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_user(users)
        if choice == "3": remove_user(users)
        if choice == "4": update_user(users)
if __name__ == '__main__':
    main()