print("Генератор персонажей")
print("У вас есть 30 очков, которые нужно распределить между характеристиками: Сила, Здоровье, Мудрость и Ловкость")

points = [["Сила",0],["Здоровье",0],["Мудрость",0],["Ловкость",0]]
choice = None
spisok_har = ["Сила", "Здоровье", "Мудрость", "Ловкость"]
score = 30
while choice != "0":
    print(
    """
    0 - Выйти
    1 - Задать или изменить характеристики персонажа
    2 - Показать итоговый набор характеристик
    """
    )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        points.clear()
        """for k in range(3,-1,-1):
                del points[k]"""
        for i in spisok_har:
            name = i
            print("\t",name)
            while True:
                print("У вас осталось {} очков".format(score))
                point = int(input("Введите кол-во очков характеристик: "))
                if score >=0 and point <= score:
                    each = (name, point)
                    points.append(each)
                    score -= point
                    break
        score = 30
    elif choice == "2":
        for each in points:
            name, point = each
            print(name,"\t", point)
            
            
