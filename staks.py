farm = []
farm.append(12)
print("добавили элемент" , farm)
farm.append(23)
print("добавили элемент" , farm)
farm.append(34)
print("добавили элемент" , farm)
print(farm)
farm.pop()
print("убрали элемент" , farm)
farm.pop()
print("убрали элемент" , farm)
farm.pop()
print("убрали элемент" , farm)
print(farm)


def summa(n):   #функция вызывает саму себя,она будет находить сумму чисел с помошью рекурсии
     if n == 0:      # когда n == 0 функция остановится, должно выполнится условие n == 0
         return 0    # выход из функции
     else:           # в остальных случаях когда n не == 0
         return n + summa(n - 1)  # будем возвращать параметр n + вызов функции с этим параметром но меньшн на 1 summa(n - 1)
print(summa(90))