# -*- coding: utf-8 -*-
import sys

hlp = """Программа - калькулятор -, +, *, /, m, rm """
ar = sys.argv
mem = 0
registr = 0

if ((len(ar)>1)and(ar[1] == "-h")):
    print (hlp)
    sys.exit(0)

def main_loop():
    while(True):
        msg = input("Что хотим делать? > ")
        disp(msg)

def disp(msg= ""):
    global registr, mem
    if (msg == "q"): sys.exit(0)
    if (msg == ""): sys.exit(0)
    if (msg == "m"):
        mem = registr
        return
    if (msg == "rm"):
        registr = mem
    else:
        fnk = get_funk(msg)
        if fnk == "Error!":
            print(fnk)
            return
        else:
            a,b = input_XY()
            registr = fnk(a,b)
            print(registr)        

def input_XY():
    a = input("Введите первое число > ")
    b = input("Введите второе число > ")
    return a,b

def get_funk(msg):
    if msg == "/": return lambda a,b: float(a) / float(b)
    if msg == "*": return lambda a,b: float(a) * float(b)
    if msg == "+": return lambda a,b: float(a) + float(b)
    if msg == "-": return lambda a,b: float(a) - float(b)
    else: return "Error!"

main_loop()

