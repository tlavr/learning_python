import time as t
import subprocess as sbp

ip_start = ["213","180","193","3"]
cmd_ping = 'ping -w 10 -n 2 '

def get_ip(st,i):
    ip = st[0] + "." + st[1] + "." + st[2] + "." + str(int(st[3])+i)
    return ip

def print_result(ip, ret):
    print(t.asctime(),'do ping for: ',ip, end = " ")

    if ret == 0: print("[OK!]",end="\n")
    else: print("[Fail!]", end="\n")

def go_subprocess(ip):
    return sbp.Popen(cmd_ping + ip, shell = True) #shell дает получать результат из процесса

def go_go(st):
    ip=""

    for i in range(10):
        ip = get_ip(st,i)
        ret = go_subprocess(ip)
        ret.wait() #zavisaet v ozhidanii razultata
        print_result(ip, ret.returncode) #returncode - peremennaya v module subprocess s rezultatom uspeh ili neudacha

tnow = t.time() #zameryaem vremya
go_go(ip_start)
tlast = t.time() - tnow
print ("\n", tlast, "\n")

lst_ip =[]
for i in range(10):
    ip = get_ip(ip_start, i)
    lst_ip.append((go_subprocess(ip), ip)) #dobavlyaem v list process i ip

tnow = t.time()
for p, ip in lst_ip:
    p.wait()
    print_result(ip, p.returncode)

tlast = t.time() - tnow
print ("\n", tlast, "\n")


        
        
    
