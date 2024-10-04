def calculate_sum(data_structure): # функция сумм данных строк и чисел
    summa = 0                      # локальная переменная
    if isinstance(data_structure, dict): #создаем цикл для проверки данных словаря для ключей и значений
        for key, value in data_structure.items():
            summa = summa + calculate_sum(key)
            summa = summa + calculate_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):  #проверяем данные списока,кортэжа,множества
        for i in data_structure:
            summa = summa + calculate_sum(i)
    elif isinstance(data_structure, int) or isinstance(data_structure, str):  #проверяем данные числа и строки
        if isinstance(data_structure, int):   # числа
            summa = summa + data_structure
        elif isinstance(data_structure, str): # строки
            summa = summa + len(data_structure)
    return summa

# Исходные данные
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
# выводим результат
result = calculate_sum(data_structure)
print(result)