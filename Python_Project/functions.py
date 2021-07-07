""" Ce programme contient toutes les fonctions qui seront appelées par le programme Menu.py"""

#!/usr/bin/python3
""" Ce programme contient toutes les fonctions qui seront appelées par le programme Menu.py"""

import subprocess
import platform

os = platform.system()
### FONCTIONS DU MENU NETWORK_AUTOAMTION ###
def gather_ip():
    if os == "Windows":
      print(subprocess.run(args="ipconfig /all", shell=True))
    elif os == "Linux":
      print(subprocess.run(args="ip a", shell=True))
      exit(0)


def gather_mac():
    print(subprocess.run(args="getmac /v", shell=True))
    exit(0)

def net_test():
    print(subprocess.run(args="ansible -i ""inventaire.ini"" all -m ping", shell=True))
    exit(0)

### FONCTIONS DU MENU SYSTEM_AUTOAMTION ###

### FONCTIONS DU MENU SECURITY_AUTOAMTION #
