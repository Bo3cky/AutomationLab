# INTRODUCTION

L’idée principale de ce projet est d'utiliser les différentes technologies à notre disposition pour permettre à l'administrateur de pouvoir automatiser une ou plusieurs tâches spécifiques sur les différents aspects d’un SI Systèmes, Réseaux, Sécurité.


Il est composé en 3 parties :
NetworkAutomation pour la partie d’administration de tâches réseaux
SystemAutomation pour la partie d’administration de tâches systèmes
SecurityAutomation pour la partie d’administration des tâches de sécurité

Pour exécuter ces tâches il suffira de sélectionner la partie pertinente pour vos tests.

il sera tout à fait possible d’étoffer le projet en ajoutant d'autres fonctionnalités.

Cette image n'est pas réprésentatitive des options actuellement mises en place dans l'outil, toutefois il sera tout à fait possible d’étoffer le projet en ajoutant d'autres fonctionnalités.

Voici une vue logique des actions possibles:

![Vue_logique_actions_script](https://user-images.githubusercontent.com/85841056/123432005-30934500-d5ca-11eb-8274-e1dbccfa1c79.png)

Chaque option appellera playbook-ansible qui sera en charge d'effectuer une lsite de tâches prédéfinies.
D’autres mécanisme ou langages pourront être implémenter.

Une fois la tâche exécutée le résultat sera stocké dans un répertoire dédier.

Par exemple supposons que l’option “Gathering_File_infos”  est sélectionnée, un playbook ansible sera donc exécuté pour récolter des informations concernant le fichier cible.

Ensuite les "gathering_facts" pertinants pour le test seront stockés dans le répertoire ./SystemDirectory les données pourront être utilisées pour faire un compartatif des fichiers existants et également reuceuillir leurs propriété.

Les possibilités sont mutiples et personnalisables.

Le projet en est à son début je suis ouvert a toutes propositions, conseils, avis d’améliorations sur ce
concept si vous êtes intéressés bien sur.

## Prérequis

### Connaissances
Avant de commencer quelques prérequis seront nécéssaires afin de bien comprendre les concepts utilisés dans ce projet

  - Être à l'aise avec la ligne de commande
  - Connaître le langage bash
  - Connaître le langage python
  - Connaître la structure de fichier YAML
  - Connaitre les bases du fonctionnement d'Ansible
  - Disposer des droits d'administrateur(root) sur la machine utilisée

### Materiel
 Voici la configuration materielle recommandée
 
  - RAM: 8Go 
  - CPU: (4coeurs/8threads)
  - Stockage: HDD/SDD
  
## Laboratoire de test

L'architechture pour le test du programme mataf.py a été mise en place a l'aide de l'outil Vagarant, un programme en ligne de commande permettant la création, la gestion, et le management, de machines virtuelles.

Ici les liens concernants la mise en place de Vagarant
  - Pour consulter la [documentation](https://www.vagrantup.com/docs)
  - Pour [l'installation](https://www.vagrantup.com/docs/installation) du logiciel Vagrant. 
  - Pour le [téléchargement](https://www.vagrantup.com/downloads) de Vagrant. 

Il faudra également télécharger un hyperviseur de type 2  (ex:Virtualbox, VmwareWorkstation) pour héberger vos VM crées par Vagarant.
  - Pour installer [Virtualbox](https://www.virtualbox.org/wiki/Downloads) 
  - Pour installer [Vmware Workstation](https://www.vmware.com/fr/products/workstation-player.html)

Une fois notre environnement installé nous devrons le configuré.

Pour télécharger ce dépot:
```
git clone https://github.com/Bo3cky/AutomationLab.git
```

## Configuration

Pour notre premeière configuration placer/créer vous dans un repertoire de votre système ou nous initialiseront l'environnement Vagrant.
  - Création du dossier pour notre environnement
```
mkdir ~/Vagrant-lab
cd ~/Vagrant-lab
```
  - Initialistion de l'environnment Vagrant sans spécifier d'image a télécharger
```
vagrant init
```

Un fichier nommé vagrant file a été créer pour définir la configuration de nos VM dès leurs lancement.

Ouvrez un éditeur de texte puis définnissez les paramètres de votre choix

Afin de simplifier le travail un [script](Vagrant-settings/Vagrantfile) est a votre disposition.

Une fois le fichier éditer ouvrez un terminal (Powershell, Bash..)
Puis entrez la commande suivante
```
vagrant up
```
Cette commande permet de configurer et de lancer les VM en s'appuyant sur le contenu du fichier vagrantfile.

Le premier lancement sera plus long que les suivants, c'est normal car les images des VM n'ont pas encore été télechargées

Si l'opération se déroule sans problèmes notre laboratoire est prêt a étre utilisé.
Il est composé de 3 machines:
  - 1 node-manager 
  - 2 nodes-clients

Enregistrer les noms d'hôtes des nodes dans le fichier de résolution /etc/hosts

Sur Linux ouvrez un terminal
```
sudo echo "192.168.0.10 node-manager" >> /etc/hosts
sudo echo "192.168.0.11 node1" >> /etc/hosts
sudo echo "192.168.0.12 node2" >> /etc/hosts
```
Sur Windows 10 ouvrez un terminal powershell en tant qu'administrateur
```
echo "192.168.0.10 node-manager" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.11 node1" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.12 node2" >> 'C:\Windows\System32\drivers\etc\hosts'
```
## Installation des packages requis

[Téléchargez](#laboratoire-de-test) ce dépot sur votre machine hôte

Copier le dossier Pyton-Project sur le node manager le mot de passe par défaut est vagrant
```bash
scp -rp Python_Project/ vagrant@node-manger:/home/vagrant
```

Conecter vous au node-manager via ssh avec l'utilisateur vagrant 
```bash
ssh vagrant@node-manager
```
Mettre a jour les dépots APT
```bah
apt-get update -y && apt-get upgarde -y
```
Installation d'ansible

```bash
apt-get install ansible
```
### Python et pip

Mise a jour de pip
```
pip install --upgrade pip
```
Installation du package [ruamel.yaml](https://github.com/commx/ruamel-yaml)
```
pip install ruamel.yaml
```
Ce package servira a modifier des valeurs dans les fichiers YAML lus par ansible
 




