#Рекурсия — это такой способ определения функции или описание функции, когда эта самая функция вызывает саму себя

def get_multiplied_digits(number):
    str_number = str(number)          # создаем переменную через строковое значение
    first = int(str_number [0])       # создаем переменную через числовое представление с первым символом str_number  0
    while str_number.endswith('0'):   # убираем нули в конце списка
        str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:           # если длина строки больше 1 вернуть 4 * 2 * 3
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first                  # если лож вывести first

result = get_multiplied_digits(420)
print(result)


#Напишите функцию get_multiplied_digits и параметр number в ней.
#Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
#Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
## из str_number в числовом представлении(int).
#Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
##Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
#4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
#Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.