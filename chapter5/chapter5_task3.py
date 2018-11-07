print("Справочник связей отец-сын")

spisok = {"Лола":"Мистер Лолипоп", "Хомяк":"Мистер Хома", "Ослик":"Мистер Ослик", "Цыпа":"Мистер Птах", "Буренка":"Мистер Бык"}
choice = None
while choice != "0":
    print(
    """
    Справочник связей отец-сын
    0 - Выход
    1 - Найти отца
    2 - Добавить связь
    3 - Изменить связь
    4 - Удалить связь
    """
    )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        son = input("Введите имя существа, отца которого вы бы хотели найти ")
        if son in spisok:
            father = spisok[son]
            print("Отца существа {} зовут {}".format(son, father))
        else:
            print("Такого существа нет в списке")
    elif choice == "2":
        son = input("Введите имя существа, которого хотите добавить в список ")
        if son not in spisok:
            father = input("Введите имя отца: ")
            spisok[son] = father
            print(spisok[son])
            print("Существо {} добавлено в словарь".format(son))
        else:
            print("Такое существо уже есть в списке!")
    elif choice == "3":
        son = input("Отца какого существа вы хотите изменить? ")
        if son in spisok:
            father = input("Введите имя отца: ")
            spisok[son] = father
        else:
            print("Такого существа еще нет в списке. Попробуйте добавить.")
    elif choice == "4":
        son = input("Введите имя существа, чью связь хотите удалить ")
        if son in spisok:
            del spisok[son]
            print("Связь удалена")
        else:
            print("Такой связи нет")
    else:
        print("Извените, в меню нет такого пункта")
input("Введите enter, чтобы выйти.")
