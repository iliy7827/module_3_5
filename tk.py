import tkinter as tk

def get_values():   #возвращающая функция которая будет получать значения из текстовых полей
    num1 = int(number1_entry.get())  # получает значение из первого поля
    num2 = int(number2_entry.get())  # получает значение из второго поля
    return num1, num2                # возвращает num1, num2

def insert_values(value):  # принимающая функция которая принимает знач value и вставляет в текстовое поле для ответа
    answer_entry.delete(0, 'end')  #очищаем текстовое поле
    answer_entry.insert(0, value)      #вставляе в текстовое поле для ответа


def add():
    num1,num2 = get_values() #возвращающая функция кот возвращает после return num1, num2
    res = num1 + num2
    insert_values(res)


def sub():
    num1,num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1,num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1,num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('калькулятор') # задаем название окна программы
window.geometry('350x350') # задаем замеры окна калькулятора
window.resizable(False,False) # ограничиваем изменение параметнов окна
button_add = tk.Button(window, text= '+', width=1, height=1, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text= '-', width=1, height=1, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text= '*', width=1, height=1, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text= '/', width=1, height=1, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=20)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=20)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=20)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=125)
number3 = tk.Label(window, text='Ответ:')
number3.place(x=100, y=275)


window.mainloop()