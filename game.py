'''Игра угадай число'''
import numpy as np
number = np.random.randint(1,101) #загадываем число

count = 0 #считаем попытки
lst = [] #уже загаданные числа
while True:
    count+=1
    predict = int(input("Введите натуральное число от 1 до 100: "))
    
    if predict > number:
        lst.append(predict)
        lst.sort()
        print("Число должно быть меньше")
        print(f'Уже загаданные числа: {lst}')
    elif predict < number:
        lst.append(predict)
        lst.sort()
        print("Число должно быть больше")
        print(f'Уже загаданные числа: {lst}')
    else:
        print(f'Загаданное число - {number}. Твое число - {predict}')
        print(f'Всего попыток - {count}')
        print('Поздравляю с победой!')
        break
    

x=1
