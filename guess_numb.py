import random as r

guess_numb = int(input('Input number from 1 to 100.\n'))
list_numb = [i for i in range(1,102)] 
#сможешь сказать почему в диапозоне 102? 
#Подсказка: надо сделать тестер самой программы
numb = max(list_numb) // 2
count = 1
while True:
    if guess_numb == numb:
        print('Maybe {}? Yes! Victory!'.format(numb)); break
    elif guess_numb > numb:
        print('Maybe {}? No. Your numb more.'.format(numb))
        list_numb = list_numb[list_numb.index(numb):]
    elif guess_numb < numb:
        print('Maybe {}? No. Your numb less.'.format(numb))
        list_numb = list_numb[:list_numb.index(numb) + 1]
    numb = max(list_numb) - len(list_numb) // 2
    count += 1
print('\nNumber guessed - {}.\nAttempts are {}.'.format(guess_numb, count))
input("Enter")
