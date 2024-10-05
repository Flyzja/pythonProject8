import math
def personal_sum(numbers):
    result_ = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result_ = result_ + i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return (result_, incorrect_data)


def calculate_average(numbers):
    try:
        sum = personal_sum(numbers)
        sum_ = sum[0]
        number = 0
        for n in numbers:
            if type(n) is int or type(n) is float:
                number = number + 1
        average = sum_ / number
        return average
    except ZeroDivisionError:
        average = 0
        return average
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
print(f'Результат 5: {calculate_average([5, 7, -12])}')


