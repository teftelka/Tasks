print("Справочник связей дед-отец-сын")

spisok = {"Лола":("Мистер Лолипоп","Дедушка Лолипоп"), "Хомяк":("Мистер Хома","Дедушка Хома"), "Ослик":("Мистер Ослик","Дедушка Ослик"), "Цыпа":("Мистер Птах","Дедушка Птахун"), "Буренка":("Мистер Бык","Дедушка Бычара")}
choice = None
while choice != "0":
    print(
    """
    Справочник связей дед-отец-сын
    0 - Выход
    1 - Найти отца
    2 - Найти деда
    3 - Добавить связь
    4 - Изменить связь
    5 - Удалить связь
    """
    )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        son = input("Введите имя существа, отца которого вы бы хотели найти ")
        if son in spisok:
            father = spisok[son][0]
            print("Отца существа {} зовут {}".format(son, father))
        else:
            print("Такого существа нет в списке")
    elif choice == "2":
        son = input("Введите имя существа, отца которого вы бы хотели найти ")
        if son in spisok:
            gr_father = spisok[son][1]
            print("Деда существа {} зовут {}".format(son, gr_father))
        else:
            print("Такого существа нет в списке")            
    elif choice == "3":
        son = input("Введите имя существа, которого хотите добавить в список ")
        if son not in spisok:
            father = input("Введите имя отца: ")
            gr_father = input("Введите имя деда: ")
            first = (father, gr_father)
            spisok[son] = first
            print("Существо {} добавлено в словарь".format(son))
        else:
            print("Такое существо уже есть в списке!")
    elif choice == "4":
        son = input("Отца и деда какого существа вы хотите изменить? ")
        if son in spisok:
            father = input("Введите имя отца: ")
            gr_father = input("Введите имя деда: ")
            first = (father, gr_father)
            spisok[son] = first
        else:
            print("Такого существа еще нет в списке. Попробуйте добавить.")
    elif choice == "5":
        son = input("Введите имя существа, чью связь хотите удалить ")
        if son in spisok:
            del spisok[son]
            print("Связь удалена")
        else:
            print("Такой связи нет")
    else:
        print("Извените, в меню нет такого пункта")
input("Введите enter, чтобы выйти.")
