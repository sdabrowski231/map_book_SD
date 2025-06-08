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


def update_user(users_data: list) -> None:
    user_name:str = input("podaj imie uzytkownika do aktualizacji:")
    for user in users_data:
        if user["name"] == user_name:
            user['name']=input("podaj nowe imie uzytkownika: ")
            user['location']=input("podaj nowe miasto uzytkownika: ")
            user['posts']=input("podaj nową liczbe postów: ")

def get_coordinates(city:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url =f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url).text

    response_html = BeautifulSoup(response,'html.parser')
    longitude=float(response_html.select('longitude')[1].text.replace(',',','))
    latitude=float(response_html.select('latitude')[1].text.replace(',',','))
    return [latitude,longitude]
def get_map(users_data:list)->None:
    import folium
    map = folium.Map(location=(52.23,21.00),zoom_start=6)
    for user in users:
        coordinates=get_coordinates(user['location'])
        folium.Marker(location=(coordinates[0],coordinates[1]),
                  popup=f" Twoj znajomy {user['name']},<br/> z miejscowości: {user['location']} <br?> opublikował {user['post']} postów").add_to(map)
    map.save("map.html")

