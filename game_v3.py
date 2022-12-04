"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    minimum = 1  # минимальное значение предполагаемого числа
    maximum = 100  # максимальное значение предполагаемого числа
    
    predict_number = np.random.randint(minimum, maximum+1)  # предполагаемое число
    
    while True:
        
        if minimum == maximum:  # корректировка на случай возникновения замкнутого цикла, из-за способа поиска нового predict_number (целочисленное деление)
            predict_number = maximum
            break
            
        elif number > predict_number:
            minimum = predict_number + 1  # устанавливает новое минимальное возможное значение предполагаемого числа
            count += 1
            predict_number = (predict_number + maximum) // 2  # новый predict_number, на середине оставшегося диапазона возмжных значений number
            continue
            
        elif number < predict_number:
            maximum = predict_number - 1  # устанавливает новое максимальное возможное значение предполагаемого числа
            count += 1
            predict_number = (predict_number + minimum) // 2  # новый predict_number, на середине оставшегося диапазона возмжных значений number
            continue
            
        elif number == predict_number:
            break  # выход из цикла если угадали
    
    return count
    
    


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел  1000

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
