# -*- coding: utf-8 -*-
import sys

hlp = """Программа - фильтрация строки """
ar = sys.argv

if (len(ar) > 1)and(ar[1] == "-h"):
    print(hlp)
    sys.exit(0)

str_w = ""
arr_w = []


def main_loop():
    while True:
        msg = input("#> ")
        dsp(msg)


def print_main_menu():
    print("1 - побайтовый ввод")
    print("2 - построчный ввод")
    print("3 - показать текущую строку")
    print("4 - показать текущий массив чисел")
    print("5 - очистить строку и массив")
    print("6 - показать главное меню")
    print("q - выход")


def dsp(msg):
    if msg == "1": byte_in()
    if msg == "2": str_in()
    if msg == "3": show_str()
    if msg == "4": show_arr()
    if msg == "5": clr_var()
    if msg == "6": print_main_menu()
    if msg == "q": sys.exit(0)


def is_d(ch):
    ch = ord(ch)
    if (ch > 47) and (ch < 58): return True
    return False


def check_d(text):
    global str_w, arr_w
    for tmp in text:
        str_w = str_w + tmp
        ln = len(str_w)
        if is_d(tmp):
            o = ord(tmp)
            if ln > 1:
                if is_d(str_w[ln-2]):
                    arr_ln = len(arr_w)
                    arr_w[arr_ln - 1] = arr_w[arr_ln - 1] * 10
                    arr_w[arr_ln - 1] = arr_w[arr_ln - 1] + o - 48
                else:
                    arr_w.append(o - 48)
            else:
                arr_w.append(o-48)


def byte_in():
    tmp = '0'
    print(r"---------Для выхода из режима побайтового ввода введите пустой символ(строку)--------")
    while tmp != '':
        tmp = input("#Введите символ> ")
        tmp_len = len(tmp)
        if tmp_len > 1:
            print("Введено больше 1 символа!")
        elif tmp_len == 0: pass
        else:
            check_d(tmp)
            show_str()
            show_arr()


def str_in():
    tmp = '0'
    print(r"---------Для выхода из режима построчного ввода введите пустую строку----------")
    while tmp != '':
        tmp = input("#Введите строку> ")
        tmp_len = len(tmp)
        if tmp_len == 0: pass
        else:
            check_d(tmp)
            show_str()
            show_arr()


def show_str():
    global str_w
    print("На данный момент введена строка: ", str_w)


def show_arr():
    global arr_w
    print("На данный момент массив чисел: ", arr_w)


def clr_var():
    global str_w, arr_w
    str_w = ""
    arr_w.clear()
    print("Строка и массив очищены!")


print_main_menu()
main_loop()


