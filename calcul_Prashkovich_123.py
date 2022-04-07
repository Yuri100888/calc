from tkinter import *

sign_oper = '+-*/'  # -> создаю для исключения задвоения знаков при вводе


# _____________Функции для кнопок:__________________


def num_1():
    screenbox.insert(END, '1')


def num_2():
    screenbox.insert(END, '2')


def num_3():
    screenbox.insert(END, '3')


def num_4():
    screenbox.insert(END, '4')


def num_5():
    screenbox.insert(END, '5')


def num_6():
    screenbox.insert(END, '6')


def num_7():
    screenbox.insert(END, '7')


def num_8():
    screenbox.insert(END, '8')


def num_9():
    screenbox.insert(END, '9')


def num_0():
    screenbox.insert(END, '0')


def num_punkt():
    screenbox.insert(END, '.')


def clear():
    screenbox.delete(0, END)


def sum():
    screen = screenbox.get()
    if '+' not in screen and '-' not in screen and '*' not in screen and '/' not in screen:
        screenbox.insert(END, '+')
    else:
        for i in screen:
            if i in sign_oper:
                redact_element = screen.index(i)
                screenbox.delete(0, END)
                screenbox.insert(END, screen[0:redact_element] + '+')


def sub():
    screen = screenbox.get()
    if '+' not in screen and '-' not in screen and '*' not in screen and '/' not in screen:
        screenbox.insert(END, '-')
    else:
        for i in screen:
            if i in sign_oper:
                redact_element = screen.index(i)
                screenbox.delete(0, END)
                screenbox.insert(END, screen[0:redact_element] + '-')


def mult():
    screen = screenbox.get()
    if '+' not in screen and '-' not in screen and '*' not in screen and '/' not in screen:
        screenbox.insert(END, '*')
    else:
        for i in screen:
            if i in sign_oper:
                redact_element = screen.index(i)
                screenbox.delete(0, END)
                screenbox.insert(END, screen[0:redact_element] + '*')


def div():
    screen = screenbox.get()
    if '+' not in screen and '-' not in screen and '*' not in screen and '/' not in screen:
        screenbox.insert(END, '/')
    else:
        for i in screen:
            if i in sign_oper:
                redact_element = screen.index(i)
                screenbox.delete(0, END)
                screenbox.insert(END, screen[:redact_element] + '/')


def back():
    text_screen = screenbox.get()
    ind = len(text_screen)
    screenbox.delete(0, END)
    screenbox.insert(END, text_screen[:ind - 1])


def rezult():
    rez_text = screenbox.get()
    for s in rez_text:
        if s == '+':
            ind = rez_text.index(s)
            rez = float(''.join(rez_text[:ind])) + float(''.join(rez_text[ind + 1:]))
            screenbox.delete(0, END)
            screenbox.insert(END, str(rez))
        if s == '-':
            ind = rez_text.index(s)
            rez = float(''.join(rez_text[:ind])) - float(''.join(rez_text[ind + 1:]))
            screenbox.delete(0, END)
            screenbox.insert(END, str(rez))
        if s == '*':
            ind = rez_text.index(s)
            rez = float(''.join(rez_text[:ind])) * float(''.join(rez_text[ind + 1:]))
            screenbox.delete(0, END)
            screenbox.insert(END, str(rez))
        if s == '/':
            ind = rez_text.index(s)
            try:
                rez = float(''.join(rez_text[:ind])) / float(''.join(rez_text[ind + 1:]))
            except ZeroDivisionError:
                screenbox.delete(0, END)
                screenbox.insert(0, 'Деление на ноль')
            else:
                screenbox.delete(0, END)
                screenbox.insert(END, str(rez))


# ------------Создание окна---------------
window = Tk()
window.title('Калькулятор')
window.geometry('300x250')
window.resizable(False, False)

# ------------Виджеты--------------------

screenbox = Entry(width=200, bg='#DCCFE1', fg='black', font='ARIAL 18', justify=RIGHT)  # -> экран калькулятора
screenbox.pack(padx=10, pady=20)

Button_table = Frame(width=50)
Button_table.pack(padx=5, pady=5)

Button_num = LabelFrame(Button_table, width=170, bg='#CFD9E1')  # -> панель кнопок с числами и запятой
Button_num.pack(padx=5, side=LEFT)

button_1 = Button(Button_num, width=5, text='1', command=num_1)
button_2 = Button(Button_num, width=5, text='2', command=num_2)
button_3 = Button(Button_num, width=5, text='3', command=num_3)
button_4 = Button(Button_num, width=5, text='4', command=num_4)
button_5 = Button(Button_num, width=5, text='5', command=num_5)
button_6 = Button(Button_num, width=5, text='6', command=num_6)
button_7 = Button(Button_num, width=5, text='7', command=num_7)
button_8 = Button(Button_num, width=5, text='8', command=num_8)
button_9 = Button(Button_num, width=5, text='9', command=num_9)
button_0 = Button(Button_num, width=13, text='0', command=num_0)
button_pukt = Button(Button_num, width=5, text=',', command=num_punkt)
button_1.grid(column=0, row=0, padx=5, pady=5)
# расположение кнопок:
button_2.grid(column=1, row=0, padx=5, pady=5)
button_3.grid(column=2, row=0, padx=5, pady=5)
button_4.grid(column=0, row=1, padx=5, pady=5)
button_5.grid(column=1, row=1, padx=5, pady=5)
button_6.grid(column=2, row=1, padx=5, pady=5)
button_7.grid(column=0, row=2, padx=5, pady=5)
button_8.grid(column=1, row=2, padx=5, pady=5)
button_9.grid(column=2, row=2, padx=5, pady=5)
button_0.grid(column=0, columnspan=2, row=3, padx=5, pady=5)
button_pukt.grid(column=2, row=3, padx=5, pady=5)

Button_oper = LabelFrame(Button_table, width=50, bg='#DDE19A')  # -> панель кнопок операций
Button_oper.pack(padx=5, side=RIGHT)
button_sum = Button(Button_oper, width=4, text='+', command=sum)
button_sub = Button(Button_oper, width=4, text='-', command=sub)
button_mult = Button(Button_oper, width=4, text='x', command=mult)
button_div = Button(Button_oper, width=4, text='/', command=div)
button_back = Button(Button_oper, width=4, text='<-', command=back)
button_clear = Button(Button_oper, width=4, text='C', bg='red', command=clear)
button_rez = Button(Button_oper, width=4, height=3, text='=', command=rezult)

# расположение кнопок
button_sum.grid(column=0, row=0, padx=5, pady=5)
button_sub.grid(column=0, row=1, padx=5, pady=5)
button_mult.grid(column=0, row=2, padx=5, pady=5)
button_div.grid(column=0, row=3, padx=5, pady=5)
button_back.grid(column=1, row=0, padx=5, pady=5)
button_clear.grid(column=1, row=1, padx=5, pady=5)
button_rez.grid(column=1, row=2, rowspan=3)

window.mainloop()
