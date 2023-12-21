import random

def гра_камінь_ножиці_папір():

    user_select = input("Виберіть Камінь, Ножиці або Папір: ").capitalize()


    if user_select not in ["Камінь", "Ножиці", "Папір"]:
        print("Невірний вибір. Будь ласка, виберіть Камінь, Ножиці або Папір.")
        return


    list_of_selection = ["Камінь", "Ножиці", "Папір"]
    random_select = random.choice(list_of_selection)


    print(f"Комп'ютер обрав: {random_select}")


    if user_select ==random_select:
        print("Нічия!")
    elif (
        (user_select == "Камінь" and random_select == "Ножиці") or
        (user_select == "Ножиці" and random_select == "Папір") or
        (user_select == "Папір" and random_select == "Камінь")
    ):
        print("Ви перемогли!")
    else:
        print("Ви програли!")


гра_камінь_ножиці_папір()