# ROCK PAPER SCISSORS

import random


ITEMS = ["Камень", "Бумага", "Ножницы"]
while True:
    x = input("Выберите предмет")
    if x == "cтоп":
        break
    y = random.choice(ITEMS)

    if x == "Камень" and y == "Ножницы":
        print("Вы победили")
    elif x == "Камень" and y == "Бумага":
        print("Вы проиграли")
    elif x == "Бумага" and y == "Камень":
        print("Вы победили")
    elif x == "Бумага" and y == "Ножницы":
        print("Вы проиграли")
    elif x == "Ножницы" and y == "Бумага":
        print("Вы победили")
    elif x == "Ножницы" and y == "Камень":
        print("Вы проиграли")
    else:
        print("Ничья")


