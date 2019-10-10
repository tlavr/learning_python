# -*- coding: utf-8 -*-
import sys, os, random

hlp = """Программа - генераторо - разбиватор """
ar = sys.argv
curdir = os.getcwd()
w_var = 0

if ((len(ar)>1)and(ar[1] == "-h")):
    print (hlp)
    sys.exit(0)

def print_main_menu():
    print("tp - тип переменной")
    print("gen - генерация чисел в массив")
    print("mtx - преобр в матрицу")
    print("dct - формирование словаря")
    print("wrt - записать в файл")
    print("clr - очистить переменную")
    print("q - выход")

print_main_menu()

def main_loop():
    while(True):
        msg = input("#> ")
        disp(msg)

def disp(msg):
    msg = msg.split(" ")
    if not validate(msg): return
    
    if msg[0] == "tp": tip()
    if msg[0] == "gen": gen_mas()
    if msg[0] == "mtx": pr_mtx()
    if msg[0] == "dct": pr_dct()
    if msg[0] == "wrt": wrt_file(msg[1])
    if msg[0] == "clr":
        global w_var
        w_var = 0
    if msg[0] == "q": sys.exit(0)

def tip():
    global w_var
    print("variable =", w_var)
    print("type of variable =" + str(type(w_var)))

    
def gen_mas():
    global w_var

    w_var = []
    for i in range(0,99,1):
        w_var.append(random.randint(10,99))
    print(w_var)  


def pr_mtx():
    global w_var
    tmp = [[0] * 9 for i in range(9)]
    
    if isinstance(w_var,list):
        for row in range(9):
            for elem in range(9):
                tmp[row][elem] = w_var[row*10 + elem]
        w_var = tmp
        for row in range(9):
            print(tmp[row])
            
    else:
        print("Variable is not a list!")
    
def pr_dct():
    global w_var
    tmp = w_var
    w_var = {"chet": [], "nechet": []}

    for i in range(len(tmp)):
        if isinstance(tmp[i],list):
            for j in range(len(tmp[i])):
                if (tmp[i][j]%2 == 0):
                    w_var["chet"].append(tmp[i][j])
                else:
                    w_var["nechet"].append(tmp[i][j])
        else:
            if (tmp[i]%2 == 0):
                w_var["chet"].append(tmp[i])
            else:
                w_var["nechet"].append(tmp[i])
    print(w_var)

def wrt_file(name):
    global w_var
    fw = open(name, 'w')
    fw.write(str(w_var))
    fw.flush()
    fw.close() 
    
    
def validate(msg):
    lst1 = ["tp","gen","mtx","dct","clr","q"]
    lst2 = ["wrt"]

    if msg == "": return False

    if lst1.count(msg[0]):
        if len(msg) == 1: return True
        else: return False
    if lst2.count(msg[0]):
        if len(msg) == 2: return True
        else: return False
    
    return False

main_loop()





    
