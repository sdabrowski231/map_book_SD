users:list=[
    {"name":"Szymon","location":"Złocieniec","posts":3},
    {"name":"Oliwier","location":"Zamość","posts":4},
    {"name":"Kuba","location":"Warszawa","posts":320},
    {"name":"Konrad","location":"Lublin","posts":12},
]
def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user['posts']} postów ")
get_user_info(users)