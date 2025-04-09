from utils.model import users
from utils.kontroller import get_user_info, add_user, remove_user,edit_user:


def main():
    get_user_info(users)
    print(f"Witaj {users[0]["name"]}")
    while True:
        print("=====menu=====")
        print("0 - zakończ program")
        print("1 - pokaż co u znajomych ")
        print("2 - dodaj nowego znajomego ")
        print("3- usun znajomego ")
        print("==============")
        choice = input("wybierz opcje MENU: ")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_user(users)
        if choice == "3": remove_user(users)

if __name__ == "__main__":
    main()
def edit_user(users_data:list)->None:
    user_tbe=input("podaj nazwe znajomego do edycji: ")

    for user in users_data:
        if user["name"]==user_tbe:
            user["name"]=input("podaj nowe imie")
            user["location"]=input("podaj nowa lokalizacje")
            user["posts"]=input("podaj nowy post")

edit_user(users)
print(users)