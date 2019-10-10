#dz : peredelat my_execute pod lubie zaprosi
# udalyat po chasti nomera

import sys, os
import sqlite3

hlp = """ Телефонный справочник SQLite """

ar = sys.argv

def db_close(con, crs, commit=0):
    if commit == 1:
        con.commit()
    else:
        crs.close()
        con.close()


def init_db_phone():
    if not os.path.exists('phone.db'):
        con = sqlite3.connect('phone.db')
        sql = """ CREATE TABLE users(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               phone INTEGER,
                               name TEXT,
                               family TEXT,
                               fio TEXT
                               );
              """
        crs = con.cursor()
        try:
            crs.execute(sql)
        except sqlite3.DatabaseError as e:
            print("ERROR:",e)
        else:
            print("Init base phone... [OK!]  \n")
        finally:
            con.commit()
            return con, crs
    else:
        con = sqlite3.connect("phone.db")
        crs = con.cursor()
        return con, crs


def print_all(table = "users"):
    con, crs = init_db_phone()
    sql = """ SELECT * FROM """ + table + """;"""
    my_execute(con,crs,sql)


def my_execute(con, crs, sql):
    try:
        crs.execute(sql)
    except sqlite3.DatabaseError as e:
        print("ERROR:",e)
    else:
        print("Выборка записей ... ")
        for row in crs:
            print(row)
    finally:
        db_close(con, crs)


def print_main_menu():
    print("1 - добавить телефон")
    print("2 - искать по номеру")
    print("3 - искать по имени")
    print("4 - искать по фамилии")
    print("5 - вывести всё")
    print("6 - удалить телефон")
    print("q - выйти")  

    
def main_loop():
    while(True):
        msg = input("#> ")
        disp(msg)

def disp(msg):
    if (msg == "1"): add_phone()
    if (msg == "2"): seek_if()
    if (msg == "3"): seek_if("fio")
    if (msg == "4"): seek_if("fio")
    if (msg == "5"): print_all()
    if (msg == "6"): dell_phone()
    if (msg == "q"): sys.exit(0)

def add_phone():
    con, crs = init_db_phone()
    name = input("#name> ")
    family = input("#family> ")
    phone = input("#phone> ")

    if not phone.isdigit(): return

    fio = name + ' ' + family
    fio = fio.upper()
    sql = """ INSERT INTO users VALUES(NULL, :phone, :name, :family, :fio); """
    req = {"phone": phone, "name": name,"family": family,"fio": fio,}
    try:
        crs.execute(sql, req)
    except sqlite3.DatabaseError as e:
        print("ERROR:",e)
    else:
        print("Запрос...[OK!]")
        print("ID ===", crs.lastrowid)
        print("Вставлено записей == ", crs.rowcount)
        print("-------------------------")
    finally:
        db_close(con,crs,1)
        print_all()

        
def seek_if(key="phone"):
    if key == "phone":
        phone = input("#phone> ")
        if not phone.isdigit(): return
        
        con, crs =  init_db_phone()
        sql = """ SELECT * FROM users WHERE phone=""" + phone + """;"""
        my_execute(con, crs, sql)
        
    if key == "fio":
        fio = input("#fio> ")
        fio = fio.upper()        
        con, crs =  init_db_phone()
        sql = " SELECT * FROM users WHERE fio LIKE '%" + fio+"%';"
        my_execute(con, crs, sql)
        
def dell_phone():
    phone = input("#phone> ")

    if phone.isalnum():
        con, crs =  init_db_phone()
        sql = """ SELECT * FROM users WHERE phone=""" + phone+ """;"""
        try:
            crs.execute(sql)
        except sqlite3.DatabaseError as e:
            print("ERROR:",e)
        else:
            if crs.fetchone() != None:
                sql = """ DELETE FROM users WHERE phone=""" + phone+ """;"""
                crs.execute(sql)
                db_close(con,crs,1)
                print_all()

print_main_menu()
init_db_phone()

main_loop()
