users:list=[
    {"name":"Szymon","location":"Złocieniec","posts":3}

]

def add_user(users_data:list)->None:
    new_name=input("podaj imie nowego znajomego: ")
    new_location=input("podaj miasto pochodzenia: ")
    new_post=int(input("podaj ilość postów: "))

    users_data.append({"name":new_name,"location":new_location,"posts":new_post})
add_user(users)
print(users)