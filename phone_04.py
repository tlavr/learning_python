# -*- coding: utf-8 -*-
import sys

hlp = """Программа - телефонный справочник """
ar = sys.argv

if ((len(ar)>1)and(ar[1] == "-h")):
    print (hlp)
    sys.exit(0)

def main_loop():
    while(True):
        msg = input("#> ")
        disp(msg)

base_ph = {"123":["Анна", "Петрова"],"456":["Стас", "Михайлов"],
           "789":["Дядя", "Вася"]}

def print_main_menu():
    print("1 - добавить телефон")
    print("2 - искать по номеру")
    print("3 - искать по имени")
    print("4 - искать по фамилии")
    print("5 - вывести все")
    print("6 - удалить телефон")
    print("q - выход")
    
print_main_menu()

def disp(msg= ""):
    if msg == "q": sys.exit(0)
    if msg == "": sys.exit(0)
    if msg == "1": add_phone() 
    if msg == "2": seek_if()
    if msg == "3": seek_if("fio")
    if msg == "4": seek_if("fio")
    if msg == "5": print_all()
    if msg == "6": dell_phone(msg)
    
def add_phone():
    global base_ph
    rec = []
    name = input("#name> ")
    family = input("#family> ")
    phone = input("#phone> ")
    
    rec.append(name)
    rec.append(family)
    base_ph[phone] = rec
    print(base_ph)

def seek_if(key="phone"):
    if key == "phone":
        phone = input("#phone> ")
        if base_ph.get(phone):
            name, f = base_ph.get(phone)
            print(name, f, phone)
        else:
            print("not found!")
    if key == "fio":
        name = input("#name> ")
        for ls in base_ph:
            fullname = base_ph.get(ls)[0] + " " + base_ph.get(ls)[1]

            if fullname.upper().find(name.upper()) >= 0:
                print(ls, fullname)

def print_all():
    for ls in base_ph:
        fullname = base_ph.get(ls)[0] + " " + base_ph.get(ls)[1]
        print(ls,fullname)

def dell_phone(phone=0):
    phone = input("#phone> ")
    if phone.isalnum():
        if base_ph.pop(phone,None) == None:
            print("phone not found!")
        else:
            print("phone ", phone, " was succesfully deleted!")
            print_all()


    
    
main_loop()

