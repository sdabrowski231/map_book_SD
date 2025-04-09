users:list=[
    {"name":"Szymon","location":"Złocieniec","posts":3},
    {"name":"Oliwier","location":"Zamość","posts":4},
    {"name":"Kuba","location":"Warszawa","posts":320},
    {"name":"Konrad","location":"Lublin","posts":12},
]

print(users)
def remove_user(users_data:list)->None:
    user_tbr=input("podaj nazwe znajomego do usunięcia: ")

    for user in users_data:
        if user["name"]==user_tbr:
            users.remove({"name":"Szymon","location":"Złocieniec","posts":3})
remove_user(users)
print(users)



#def add_user(users_data:list)->None:
#    new_name=input("podaj imie nowego znajomego: ")
#    new_location=input("podaj miasto pochodzenia: ")
#    new_post=int(input("podaj ilość postów: "))
#
#   users_data.append({"name":new_name,"location":new_location,"posts":new_post})
#add_user(users)
#print(users)

#moja_lista_na_sok=["banan","marchew","zytnia"]



