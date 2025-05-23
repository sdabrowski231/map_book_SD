from utils.model import users
from utils.kontroller import get_user_info, add_user, remove_user,edit_user:


def main():
    get_user_info(users)
    print(f"Witaj {users[0]["name"]}")
    while True:
        print("=====menu=====")
        print("0 - zakończ program")
        print("1 - pokaż co u znajomych ")
            choice = input("wybierz opcje MENU: ")
            if choice == "0": break
            if choice == "1": get_user_info(users)


if __name__ == '__main__':
    main()