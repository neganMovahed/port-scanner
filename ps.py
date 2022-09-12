from socket import *
from colorama import Fore
import os
try:
    os.system("cls")
    print(Fore.LIGHTGREEN_EX+"""
PORT SCAN
    """)
    # maede
    host = input(Fore.WHITE+"Enter Your target: ")
    range_aval = input("Enter your range (1): ")
    range_dovom = input("Enter your range (2): ")
    for i in range(int(range_aval), int(range_dovom)):
        sock_POBT = socket(AF_INET,SOCK_STREAM)
        con = sock_POBT.connect_ex((host,i))
        print()
        # maede movahed
        if con == 0:
            servisname = getservbyport(i)
            print(Fore.LIGHTGREEN_EX+"[<=>] port " , i , servisname , " open ")
        else:
            print(Fore.LIGHTRED_EX+"[-] port ", i , " close ")
except :
    print("check Host or internet ")