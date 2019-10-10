# -*- coding: utf-8 -*-
import sys, traceback

hlp = "Программа - перехватчик сообщений"

ar = sys.argv

if ((len(ar)>1) and (ar[1] == "-h")):
    print(hlp)
    sys.exit(0)

def tmp1():
    "Zero_Division_Error"
    x = 1/0

def tmp2():
    "StopIteration"
    fd = open(r"sadsd.txt","w+")
    fd.flush()
    fd.close()
    fd = open(r"sadsd.txt", "r+")
    for f in range(10):
        x = fd.__next__()
        print(x)
    fd.flush()
    fd.close()

def tmp3():
    "OSError"
    fd = open("dwh.txt", "r")

def tmp4():
    "NameError"
    x = a + 1

def tmp5():
    "IOError"
    fd = open(r"sadsd.txt", "r")
    fd.flush()
    fd.close()

def tmp6():
    "ImportError"
    import asdsadas

def tmp7():
    "KeyError"
    x ={"1": "dwg", "2": "dasd"}
    print(x["3"])

def tb_format(cls, val, tb):
    desc =[]
    for i in traceback.format_exception(cls, val, tb, limit=15): desc.append(i)
    for i in desc: print(i)
    return desc

base_func = {
    1: lambda : tmp1(),
    2: lambda : tmp2(),
    3: lambda : tmp3(),
    4: lambda : tmp4(),
    5: lambda : tmp5(),
    6: lambda : tmp6(),
    7: lambda : tmp7()
}

for prg in base_func:
    try:
        base_func[prg]()
    except Exception as e:
        cls, val, tb = sys.exc_info()
        #print(e.__class__.__name__)
        #tb_format (cls, val, tb)
        #print(cls, val, tb)
        print (e.__doc__)

#дз доработать свой класс исключений и попробовать использовать raise для выброса пользовательского исключения
# d108295@yandex.ru почта Виталия Геннадьевича