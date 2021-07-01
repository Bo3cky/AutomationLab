""" Ce programme représente la pièce centrale de l'application il permettera de séléctionner les
différentes actions via un menu intéractif. """

""" Nous aurons besoin d'importer quelques modules pour rendre ce programme foctionnel:
    - Le module "getpass" permettant l'implémentation de mot de passe
    - Le module "hashlib" permettant l'implémentation du chiffrement de mots de passe """

import os
import hashlib
from getpass import getpass


print("Bienvenue dans la console d'automatisation 1.0")


def menu():
  print("MENU PRINCIPAL\n")
  print("1 - Network-automation")
  print("2 - System-automation")
  print("3 - Security-automation")
  print("4 - Exit\n")

def menu_net():
  print("MENU NETWORKING\n")
  print("1 - Gathering-IP")
  print("2 - Gathering-MAC")
  print("3 - Connectivity_tests")
  print("4 - Return to main menu\n")

def menu_sys():
  print("MENU SYSTEM\n")
  print("1 - Gathering-user")
  print("2 - Gathering-file")
  print("3 - Create services")
  print("4 - Return to main menu\n")

def menu_sec():
  print("MENU SECURITY\n")
  print("1 - Nmap-scan")
  print("2 - Rkhunter-scan")
  print("3 - Return to main menu\n")

### Demande de mot de passe pour accèder au programme ###

chaine_mot_de_passe = b"automation2021"
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
verrouille = True

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
print("Mot de passe accepté\n")

### MENU PRINCIPAL ###
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

  if choice == 1: ### MENU NETOWRKING ###
    menu_net()
    choice2 = input("Choisissez une action d'automatisation: ")
    if choice2 == 1:
      #do task 1
     pass
  
  elif choice == 2: ### MENU SYSTEM ###
    menu_sys()
    choice3 = input("Choisissez une action d'automatisation: ")
  
  elif choice == 3: ### MENU SECURITY ###
    menu_sec()
    choice4 = input("Choisissez une action d'automatisation: ")
  
  elif choice == 4: ### EXIT ###
    answer = input("Voulez vous quitter ce programme? (O/N): ")
    answer = str(answer)
    if answer == "O" :
      print("\nMerci d'avoir utilisé ce programme ! \nA bientôt !")
      break
    else:
      continue

os.system("pause")


