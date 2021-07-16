#!/usr/bin/python3
""" Ce programme représente la pièce centrale de l'application il permettera de séléctionner les
différentes actions via un menu intéractif ou en ligne de commande. """

"""Nous aurons besoin d'importer quelques modules pour rendre ce programme foctionnel:
    - Le module "getpass" permettant l'implémentation de mot de passe
    - Le module "hashlib" permettant l'implémentation du chiffrement de mots de passe
    - Le module "functions" permettant l'utilisation de nos fonctions pour éxécuter la tâche sélectionnée
    - Le module "argpase" permmettant d'utiliser notre programme en ligne de commande avec différentes options """

import hashlib
from getpass import getpass
import functions 
import argparse


### CREATION D'UNE FONCTION POUR LA DEMANDE DE MOT DE PASSE ### 

def passwd():
  chaine_mot_de_passe = b"exemple"

  """A titre d'exemple le mot de passe est affiché en clair, cependant pour un environnement en production
   évitez de renseigner le mot de passe avec cette méthode, choisissez
   un autre moyen (ex: fichier crypté contenant le mot de passe, ect...)"""
  mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
  verrouille = True
  essais = 3

  while verrouille:
  # la fonction getpass permet de définir un mot de passe sans visuel sur les caractères tapés. 
     entre = getpass("Veuillez entrez le mot de passe pour dévérouiller le programme: ") # automation2021
    # On encode la saisie pour avoir un type bytes
     entre = entre.encode()
    
     entre_chiffre = hashlib.sha1(entre).hexdigest()
     if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
     else:
        print("Mot de passe incorrect")
        essais -= 1
        print('il ne vous reste {} essais'.format(essais))
        if essais == 0:
          print("Trop de tentatives effectué rééssayez dans 5 min")
          exit(0)
  print("Mot de passe accepté\n")

### CREATION DES ARGUMENTS POUR L'UTILISATION EN LIGNE DE COMMANDE ### 

parser = argparse.ArgumentParser(description='Cet outil permet d\'automatiser plusieurs tâches d\'administration.')
parser.add_argument('--gip', help="Affiche la coniguration IP de l'hôte", action="store_true")
parser.add_argument('--menumode', help="Passe en mode menu", action="store_true")
parser.add_argument('--gmac', help="Affiche les addresses mac de l'hôte", action="store_true")
parser.add_argument('--depkey', help="Déploiement de clé ssh sur les nodes", action="store_true")
parser.add_argument('--checksum', help="Permet de vérifier l'intégrité de fichiers", action="store_true")

args = parser.parse_args()
if args.gip:
  passwd()
  functions.gather_ip()
  exit(0)
elif args.gmac:
  passwd()
  functions.gather_mac()
  exit(0)
elif args.depkey:
  passwd()
  functions.ssh_deploy_key()
  exit(0)
elif args.checksum:
  passwd()
  functions.gathering_file()
  exit(0)
elif args.menumode:
  passwd()
  pass
else:
  exit

### CREATION DES FONCTIONS POUR L'AFFICHAGE DES DIFFERENTS MENUS ### 

print("Bienvenue dans la console d'automatisation 1.0")


def menu():
  print("MENU PRINCIPAL\n")
  print("1 - Network-automation")
  print("2 - System-automation")
  print("3 - Security-automation")
  print("4 - Exit\n")

def menu_net():
  print("MENU NETWORKING\n")
  print("1 - Gathering-IP (Comming soon...)")
  print("2 - Gathering-MAC (Comming soon...)")
  print("3 - SSH-Deploy-keys")
  print("4 - Return to main menu\n")

def menu_sys():
  print("MENU SYSTEM\n")
  print("1 - Gathering-user (Comming soon...)")
  print("2 - Gathering-file-checksum")
  print("3 - Create services (Comming soon...)")
  print("4 - Return to main menu\n")

def menu_sec():
  print("MENU SECURITY\n")
  print("1 - Nmap-scan (Comming soon...)")
  print("2 - Rkhunter-scan (Comming soon...)")
  print("3 - Return to main menu\n")



### MENU PRINCIPAL ###
passwd()
while True:
  menu()
  while True:
    """ prévention d'erreur de frappe pour la sélection d'un menu d'automatisation,
     ici un chiffre est attendu en réponse"""
    try: 
      choice = input("Choisissez un menu d'automatisation: ")
      choice = int(choice)
    except ValueError:
     print("\nVeuillez entrer un chiffre")
    else:
        break

### MENU NETOWRKING ###
  if choice == 1:
    menu_net()
    choice2 = int(input("Choisissez une action d'automatisation: "))
    if choice2 == 1:
      functions.gather_ip()
    elif choice2 == 2:
      functions.gather_mac()
    elif choice2 == 3:
      functions.ssh_deploy_key()
    else:
     pass

### MENU SYSTEM ###
  elif choice == 2: 
    menu_sys()
    choice3 = input("Choisissez une action d'automatisation: ")
    #if choice3 == 1:
     # functions.gather_ip()
    if choice3 == 2:
      functions.gathering_file()
    #elif choice3 == 3:
     # functions.ssh_deploy_key()
    else:
     pass

### MENU SECURITY ###  
  elif choice == 3: 
    menu_sec()
    choice4 = input("Choisissez une action d'automatisation: ")
    if choice4 == 1:
     pass 
    elif choice4 == 2:
     pass 
    elif choice4 == 3:
     pass 
    else:
     pass
### EXIT ###
  elif choice == 4:
    answer = input("Voulez vous quitter ce programme? (o/n): ")
    answer = str(answer)
    if answer == "o":
      print("\nMerci d'avoir utilisé ce programme ! \nA bientôt !")
      break
    else:
      continue





