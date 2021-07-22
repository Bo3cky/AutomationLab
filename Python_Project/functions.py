#!/usr/bin/python3
""" Ce programme contient toutes les fonctions qui seront appelées par le programme Menu.py"""
import os
import subprocess
import platform
from filecompare import file_analysis
import ruamel.yaml
import filecmp
import sys

### FONCTION DE REDIRECTION ###

def net_redirect():
      state = sys.argv[3]
      task = subprocess.run(args="sudo cp /home/vagrant/vagrant  /home/vagrant/{}.copy".format(state), shell= True)
      task2 = subprocess.run(args="sudo cp /home/vagrant/vagrant.pub /home/vagrant/{}.pub.copy".format(state), shell= True)
      task3 = subprocess.run(args="sudo mv /home/vagrant/*.copy /home/vagrant/NetworkDirectory/", shell=True)
      task4 = subprocess.run(args="sudo chown vagrant:vagrant /home/vagrant/NetworkDirectory/{}.copy".format(state), shell=True)
      task5 = subprocess.run(args="ssh-add /home/vagrant/NetworkDirectory/{}.copy".format(state), shell=True)
      if task and task2 and task3 and task4 and task5:
        print("La clé publique et privée de l'utilisa(teur/trice) {} ont été copier et enregistrées dans le repertoire NetworkDirectory/".format(state))
        print("La clé privéé de l'utilisa(teur/trice) {} a été embarqué sur votre agent ssh".format(state))
        exit(0)
      else:
        print("la redirection a échouée")

def sys_redirect():

      task = subprocess.run(args="mv checksum2.txt checksum3.txt SystemDirectory/", shell=True)
      if task:
         print("Vos fichers checksum ont été enregistrés dans le repertoire SystemDirectory/")
         exit(0)
      else:
         print("la redirection a échouée")

OS = platform.system()
### FONCTIONS DU MENU NETWORK_AUTOAMTION ###
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
    net_redirect()
    exit(0)

def set_state_ssh(state):
    file_name = "gendistkey-ssh.yml"
    with open(file_name) as Cf:
      doc = ruamel.yaml.load(Cf, Loader=ruamel.yaml.RoundTripLoader)
      doc[0]["tasks"][1]["name"] = "Creation de l'utilisateur " + state
      doc[0]["tasks"][1]["user"]["name"] = state
      doc[0]["tasks"][2]["name"] = "Ajout de l'utilisateur '{}' aux sudoers".format(state)
      doc[0]["tasks"][2]["copy"]["dest"] = "/etc/sudoers.d/{}".format(state)
      doc[0]["tasks"][2]["copy"]["content"]= '{} ALL=(ALL) NOPASSWD: ALL'.format(state)
      doc[0]["tasks"][3]["authorized_key"]["user"]= state
    with open (file_name, "w") as Cf:
      ruamel.yaml.dump(doc, Cf, allow_unicode= True, Dumper=ruamel.yaml.RoundTripDumper)
      
### FONCTIONS DU MENU SYSTEM_AUTOAMTION ###
def set_state(state):
    file_name = "Checksum-file.yml"
    with open(file_name) as Cf:
      doc = ruamel.yaml.load(Cf, Loader=ruamel.yaml.RoundTripLoader)
      doc[0]["tasks"][0]["stat"]["path"]= state
    with open (file_name, "w") as Cf:
      ruamel.yaml.dump(doc, Cf, allow_unicode= True, Dumper=ruamel.yaml.RoundTripDumper)

def gathering_file():
    print(subprocess.run(args=" ansible-playbook -i inventaire.ini Checksum-file.yml | ./tri.sh ", shell=True ))
    file_analysis()
    sys_redirect()
    exit(0)

### FONCTIONS DU MENU SECURITY_AUTOAMTION ###

