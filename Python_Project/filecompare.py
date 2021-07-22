#!/usr/bin/python3

""" module permettant de comparer deux fichiers """

import filecmp
import shutil
import os
from pathlib import Path
from datetime import *

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f1 = 'checksum.txt'
f2 = r'checksum2.txt'
f2Obj = Path(f2)
f3 = r'checksum3.txt'
f3Obj = Path(f3)

def file_analysis():
  if not f2Obj.exists():

    shutil.copyfile(f1, f2)
    print("\nle fichier {} a été copier sous le nom de {} dans {}".format(f1, f2, os.getcwd()))
    print("\nVeulliez relancer ce scan pour comparer l'intégrité du fichier ")
    exit(0)

  else:
    pass

  if not f3Obj.exists():

    shutil.copyfile(f1, f3)
    print("\nLe fichier existe déjà, vérification de l'intégrité en cours ...")
    comparatif = filecmp.cmp(f2,f3)

  if comparatif:
    print("\nl'intégrité du fichier est valide")
  else:
    print("\nAttention! Un ou plusieurs fichiers on été modifiés!\n")

  if comparatif is False:
    with open('checksum2.txt', 'r') as c2:
       print("Fichier-01:")
       print(c2.read(),"\n")
    c2.close()

    with open('checksum3.txt', 'r') as c3:
       print("Fichier-02:")
       print(c3.read(),"\n")
    c3.close()
    print("Scan du: {} \nHoraire: {}".format(today, current_time))

