'''Игра угадай число'''
'''Играет компьютер'''
import numpy as np

def game(number:int=1) -> int:
    """Указываем число, которое комп должен отгадать

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: одна реализация функции - одна игра компьютера с выводом кол-ва попыток
    """
    count=0
    while True:
        count+=1
        predict = np.random.randint(1,101)
        if number == predict:
            break
    return count

def simul(game, size) -> int:
    """проверяем среднее кол-во поптыток до угадывания у нашего алгоритма

    Args:
        game (_type_): функция угадывания
        size (_type_): размер выборки

    Returns:
        int: среднее кол-во попыток в size симуляциях игры 
    """
    
    lst = []
    # np.random.seed(1) # для воспроизводимости результата
    predict_array = np.random.randint(1,101, size=(size))
    for number in predict_array:
        lst.append(game(number))
    score = round(np.mean(lst),2)
    print(f'Наш алгоритм угадывает число в среднем за {score} попыток')
    return score

simul(game,1000)
# if __name__=='__main__':
#     simul(game,1000)
