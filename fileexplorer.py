# -*- coding: utf-8 -*-
import sys, os, subprocess, time

hlp = """Программа - файловый менеджер """
ar = sys.argv
curdir = os.getcwd()
curdirs = []

if ((len(ar)>1)and(ar[1] == "-h")):
    print (hlp)
    sys.exit(0)

def print_main_menu():
    print("ls - содержимое каталога")
    print("prp - копирование файла")
    print("opn - открыть файл")
    print("crt - создать файл или каталог")
    print("dell - удалить файл")
    print("up - выйти из текущего каталога")
    print("dwn - войти в каталог")
    print("q - выход")

print_main_menu()

def main_loop():
    while(True):
        msg = input("#> ")
        disp(msg)

def disp(msg):
    msg = msg.split(" ")
    if not validate(msg): return
    
    if msg[0] == "ls": list_dir()
    if msg[0] == "prp": property_file(msg[1])
    if msg[0] == "opn": open_file(msg[1])
    if msg[0] == "crt": create(msg[1])
    if msg[0] == "up": up_dir()
    if msg[0] == "dwn": down_dir(msg[1])
    if msg[0] == "dell": dell_file(msg[1])
    if msg[0] == "q": sys.exit(0)

def list_dir(): 
    global curdir, curdirs
    lst= []
    item = ""
    for item in os.listdir(curdir):
        if os.path.isdir(item):
            curdirs.append(item)
            item = "[" + item + "]"
        lst.append(item)
    lst.reverse()
    
    for item in lst:
        print(item)

def up_dir():
    global curdir
    curdir = os.getcwd()
    lst = curdir.split("\\")
    path = ""

    for i in range(0,len(lst)-1,1):
        path = path + lst[i] + "\\"

    os.chdir(path)
    curdir = os.getcwd()
    list_dir()

def down_dir(name):
    global curdir

    lst = curdir.split("\\")

    if name == lst[len(lst)-1]: return
    if not curdirs.count(name): return

    path = os.getcwd() + "\\" + name
    os.chdir(path)
    curdir = os.getcwd()

    list_dir()

def open_file(name=""):
    global curdir
    name = curdir + "\\" + name
    name = name.strip()
    subprocess.Popen(r"notepad.exe " + name)

def property_file(name):
    global curdir
    path = curdir + "\\" + name
    if not os.path.exists(r"" + path): return
    else:
        prp = os.stat(r"" + path)
        print("размер файла - ", prp.st_size)
        print("последнее открытие - ",
              time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(prp.st_atime)))
        print("создание файла - ",
              time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(prp.st_ctime)))
        print("изменение файла - ",
              time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(prp.st_mtime)))
        
def create(name):
    lst = name.split(".")
    if len(lst) > 2: return
    if len(lst) == 2:
       if len(lst[1]) > 3: return
       fd = open(curdir + lst[0] + "." + lst[1], "w+")  
       fd.flush()
       fd.close()

    if len(lst) == 1:
        os.mkdir(curdir + lst[0])

def validate(msg):
    lst1 = ["ls", "up", "q"]
    lst2 = ["prp", "opn", "crt", "dell", "dwn"]
    
    
    if msg == "": return False

    if lst1.count(msg[0]):
        if len(msg) == 1: return True
        else: return False
    
    if lst2.count(msg[0]):
        if len(msg) == 2: return True
        else: return False

    return False

def dell_file(msg):
    os.remove(msg)

main_loop()





    
