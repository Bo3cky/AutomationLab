#!/usr/bin/python3
""" Ce programme représente la pièce centrale de l'application il permettera de séléctionner les
différentes actions via un menu intéractif. """

"""Quelques modules seront nécéssaires pour rendre ce programme foctionnel:
    - Le module "getpass" permettant l'implémentation de mot de passe
    - Le module "hashlib" permettant l'implémentation du chiffrement de mots de passe
    - Le module "functions" permettant l'utilisation de nos fonctions pour éxécuter la tâche sélectionnée
    - Le module "argpase" permmettant d'utiliser notre programme en ligne de commande avec différentes options 
    - Le module "sys" permmettant d'intéragir avec les entrées et les sorties du système 
    - Le module "subprocess" permmettant d'éxcuter des commandes sur le système """
    
import hashlib
from getpass import getpass
import functions
import argparse
import sys
import subprocess

                    #### DEMANDE DE MOT DE PASSE POUR L'ACCES AU PROGRAMME ####
"""
def passwd():
  chaine_mot_de_passe = b"exemple"

  """"""A titre d'exemple le mot de passe est affiché en clair, dans un environnement en production
   évitez de renseigner le mot de passe avec cette méthode, choisissez
   un autre moyen (ex: fichier crypté contenant le mot de passe...)""""""
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
"""

                                        #### DEFINITION DES ARGUMENTS ####
    
parser = argparse.ArgumentParser(description='Cet outil permet d\'automatiser plusieurs tâches d\'administration.')
parser.add_argument("VAR", help="ajout d'une variable" ,type=str, nargs="?")
#parser.add_argument('-i','--gip', help="Affiche la coniguration IP de l'hôte", action="store_true")
#parser.add_argument('-m','--gmac', help="Affiche les addresses mac de l'hôte", action="store_true")
parser.add_argument('-U','--user', help="Utilisateur cible", action="store_true")
parser.add_argument('-dk','--depkey', help="Déploiement de clé ssh sur les nodes", action="store_true")
parser.add_argument('-c','--checksum', help="Permet de vérifier l'intégrité de fichiers", action="store_true")
parser.add_argument("-f","--file", help="specifiez un fichier que vous souhaitez vérifier" , action="store_true")
parser.add_argument("-M","--menumode", help="Passez en mode menu" , action="store_true")
args = parser.parse_args()
#if args.gip:
#  passwd()
#  functions.gather_ip()
#  exit(0)
#elif args.gmac:
#  passwd()
#  functions.gather_mac()
#  exit(0)
if args.depkey and args.user:
#  passwd()
    var_selected_ssh = sys.argv[3]
    functions.set_state_ssh(var_selected_ssh)
    functions.ssh_deploy_key()
    exit(0)
elif args.checksum and args.file:
#  passwd()
    var_selected = sys.argv[3]
    functions.set_state(var_selected)
    functions.gathering_file()
    exit(0)
elif args.menumode:
#  passwd()
  pass
else:
  exit(0)

                                        #### DEFINITION DES MENUS ####
    
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




# passwd()
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
                                    #### CHOICES IN MENU NETOWRKING ####
  if choice == 1: 
    menu_net()
    choice2 = int(input("Choisissez une action d'automatisation: "))
    if choice2 == 1:
      functions.gather_ip()
    elif choice2 == 2:
      functions.gather_mac()
    elif choice2 == 3:
      user = str(input("Sur quel utilsateur voulez vous déployer la clé SSH?: "))
      subprocess.run(args="./mataf.py -dk -U {}".format(user), shell=True)
    else:
     pass
                                    #### CHOICES IN MENU SYSTEM ####
  elif choice == 2: 
    menu_sys()
    choice3 = int(input("Choisissez une action d'automatisation: "))
    if choice3 == 2:
      file = str(input("Quel fichier voulez vous vérifier?: "))
      subprocess.run(args="./mataf.py -c -f {}".format(file), shell=True)

                                    #### CHOICES IN MENU SYSTEM ####
  elif choice == 3: 
    menu_sec()
    choice4 = input("Choisissez une action d'automatisation: ")

                                        #### EXIT ####
  elif choice == 4: 
    answer = input("Voulez vous quitter ce programme? (y/n): ")
    answer = str(answer)
    if answer == "y" :
      print("\nMerci d'avoir utilisé ce programme ! \nA bientôt !")
      break
    else:
      continue






