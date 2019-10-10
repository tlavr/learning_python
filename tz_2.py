# -*- coding: utf-8 -*-
import sys, os, random, math, subprocess

hlp = """Программа - генератор - работа с файлами """
ar = sys.argv
w_var = 0
w_filt = 0
curdir = os.getcwd()
name_f1 = ''


if (len(ar) > 1) and (ar[1] == "-h"):
    print(hlp)
    sys.exit(0)


def print_main_menu():
    print("gen  - инициализация двумерного массива")
    print("filt - формирование второго массива")
    print("lst  - показать содержимое каталога")
    print("opn  - открыть файл")
    print("dlt  - удалить файл")
    print("mm   - показать главное меню")
    print("q    - выход")


print_main_menu()


def main_loop():
    while (True):
        msg = input("#> ")
        disp(msg)


def disp(msg):
    msg = msg.split(" ")
    if not validate(msg): return

    if msg[0] == "gen": gen_mas()
    if msg[0] == "filt": mas_flt()
    if msg[0] == "dlt": dell_file()
    if msg[0] == "lst": list_dir()
    if msg[0] == "opn": open_file()
    if msg[0] == "mm": print_main_menu()
    if msg[0] == "q": sys.exit(0)


def gen_mas():
    global w_var
    n = int(input("#Введите размерность массива > "))
    d = int(input("#Введите верхнее ограничение диапазона значений > "))
    w_var = []
    for i in range(0, n ** 2, 1):
        w_var.append(random.randint(0, d))
    pr_mtx()
    wrt_file(w_var)


def pr_mtx(var=[]):
    global w_var
    ret = True
    if not var:
        ret = False
        var = w_var
    n = int(math.sqrt(len(var)))
    tmp = [[0] * n for i in range(n)]

    if isinstance(var, list):
        for row in range(n):
            for elem in range(n):
                tmp[row][elem] = var[row * n + elem]
        if not ret:
            w_var = tmp
            for row in range(n):
                print(tmp[row])
        else:
            var = tmp
        if ret:
            return var
    else:
        print("Variable is not a list!")


def mas_flt():
    global name_f1, w_filt, w_var
    w_filt = []
    c = []
    if not name_f1:
        print(" ---- Сначала выполните процедуру инициализации массива!!!----")
        return
    print("-----Введите два числа, которые нужно выбрать из массива------")
    a = int(input("# Введите первое число > "))
    b = int(input("# Введите второе число > "))

    sz = os.path.getsize(name_f1)
    fd = open(name_f1, "r")
    tmp = str(fd.read())
    fd.flush()
    fd.close()

    for i in tmp:
        if i.isalnum():
            c.append(int(i))
    tmp = pr_mtx(c)

    for i in range(len(tmp)):
        if isinstance(tmp[i], list):
            for j in range(len(tmp[i])):
                if (tmp[i][j] == a)or(tmp[i][j] == b):
                    w_filt.append(tmp[i][j])
    wrt_file(w_filt)


def wrt_file(var):
    global w_var, name_f1, w_filt
    name = input("# Введите имя файла для записи > ")
    name_f1 = name
    fw = open(name, 'w')
    fw.write(str(var))
    fw.flush()
    fw.close()
    print("# Массив", str(var), " успешно создан и записан в файл ", name, " !")


def dell_file():
    name = input("# Введите имя файла для удаления > ")
    tmp = name.split('.')
    if tmp[1] == 'txt':
        os.remove(name)


def list_dir():
    global curdir
    lst = []
    item = ""
    for item in os.listdir(curdir):
        if os.path.isdir(item):
            item = "[" + item + "]"
        lst.append(item)
    lst.reverse()

    for item in lst:
        print(item)


def open_file():
    global curdir
    name = input("# Введите имя файла > ")
    name = curdir + "\\" + name
    name = name.strip()
    subprocess.Popen(r"notepad.exe " + name)


def validate(msg):
    lst1 = ["gen", "filt", "dlt", "lst", "opn", "mm", "q"]

    if msg == "": return False

    if lst1.count(msg[0]):
        if len(msg) == 1:
            return True
        else:
            print("Введите пункт из меню без ничего лишнего! Окно выбора файла отроется потом!")
            print_main_menu()
            return False
    return False


main_loop()






