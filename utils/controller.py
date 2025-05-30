def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user['posts']} postów ")


def add_user(users_data: list) -> None:
    new_name = input("podaj imie nowego znajomego: ")
    new_location = input("podaj miasto pochodzenia: ")
    new_post = int(input("podaj ilość postów: "))
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_post})

def remove_user(users_data: list) -> None:
    user_name:str = input("podaj nazwe znajomego do usunięcia: ")

    for user in users_data:
        if user["name"] == user_name:
            users_data.remove({"name": "Szymon", "location": "Złocieniec", "posts": 3})



