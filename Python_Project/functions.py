#!/usr/bin/python3
""" Ce programme contient toutes les fonctions qui seront appelées par le programme Menu.py"""
import os
import subprocess
import platform
from filecompare import file_analysis
import getpass
import hashlib

OS = platform.system()

### FONCTIONS DU MENU NETWORK_AUTOAMTION ###  (en cours de développement)
def gather_ip():
    if OS == "Windows":
      print(subprocess.run(args="ipconfig /all", shell=True))
    elif OS == "Linux":
      print(subprocess.run(args="ip a", shell=True))
      exit(0)

def gather_mac():
    print(subprocess.run(args="getmac /v", shell=True))
    exit(0)

def ssh_deploy_key():
    print(subprocess.run(args="ansible-playbook -i inventaire.ini gendistkey-ssh.yml", shell=True))
    exit(0)

### FONCTIONS DU MENU SYSTEM_AUTOAMTION ###

def gathering_file():
    print(subprocess.run(args=" ansible-playbook -i inventaire.ini Checksum-file.yml | ./tri.sh ", shell=True ))
    file_analysis()
    exit(0)
### FONCTIONS DU MENU SECURITY_AUTOAMTION ### (en cours de développement)
