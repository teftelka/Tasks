import random as r
print ("Вывод слов в случайном порядке")

WORDS = ["солнце", "луна", "печенька", "луна", "картина", "бобр", "лосось", "панда", "грибочек", "огонь"]
new_list = []
count = 0
print("Исходный список выглядит так \n",WORDS)
input("Введите Enter, чтобы увидеть словав случайном порядке без повторений")
while WORDS:
    word = r.choice(WORDS)
    if word in new_list:
        WORDS.remove(word)
    else:
        new_list.append(word)
        count += 1
for i in new_list:
    print(i)

input("Введите Enter, чтобы выйти")
