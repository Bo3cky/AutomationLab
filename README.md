# PRESENTATION

L’idée principale de ce projet est d'utiliser les différentes technologies à notre disposition pour permettre à l'administrateur de pouvoir automatiser une ou plusieurs tâches spécifiques sur différents aspects d’un SI Systèmes, Réseaux, Sécurité.


le programme [mataf.py](https://github.com/Bo3cky/AutomationLab/blob/main/Python_Project/mataf.py) 3 parties :

- NetworkAutomation pour la partie d’administration de tâches réseaux
- SystemAutomation pour la partie d’administration de tâches systèmes
- SecurityAutomation pour la partie d’administration des tâches de sécurité

Cette image n'est pas réprésentative des options actuellement mises en place dans l'outil.

Voici une vue logique des actions possibles:

![IMAGE1](https://github.com/Bo3cky/AutomationLab/blob/main/Images/Vue_logique_actions_script.png)

Chacune des options s'appuient sur plusieurs processus (playbook-ansible, script bash) afin d'effectuer une liste de tâches prédéfinies.
D’autres mécanismes ou langages de programmation pourront être implémentés.

Une fois la tâche exécutée le résultat sera stocké dans un répertoire dédié.


### Connaissances
Avant de commencer quelques prérequis seront nécéssaires afin de bien comprendre les concepts utilisés dans ce projet

  - Connaître le langage bash
  - Connaître le langage python
  - Connaître la structure de fichier YAML
  - Connaitre les bases du fonctionnement d'Ansible
  - Disposer des droits d'administrateur(root) sur la machine utilisée
  - Être à l'aise avec la ligne de commande est un plus

### Materiel
 Voici la configuration matérielle recommandée pour l'installation du laboratoire de tests
 
  - RAM: 8Go 
  - CPU: (4coeurs/8threads)
  - Stockage: HDD/SDD
 
## Laboratoire de test

L'architecture mise en place pour le test du programme mataf.py a été construite à l'aide de l'outil Vagrant, un programme en ligne de commande permettant la création, la gestion, et le management, de machines virtuelles.

Ici les liens concernants la documentation et l'installation de Vagrant
  - Pour consulter la [documentation](https://www.vagrantup.com/docs)
  - Pour [l'installation](https://www.vagrantup.com/docs/installation) du logiciel Vagrant. 
  - Pour le [téléchargement](https://www.vagrantup.com/downloads) de Vagrant. 

Il faudra également télécharger un hyperviseur de type 2  (ex:Virtualbox, VmwareWorkstation) pour héberger les VM crées par Vagrant.
  - Pour installer [Virtualbox](https://www.virtualbox.org/wiki/Downloads) 
  - Pour installer [Vmware Workstation](https://www.vmware.com/fr/products/workstation-player.html)

Une fois notre environnement installé il devra être configuré.


## Configuration

Pour télécharger ce dépot:
```bash
git clone https://github.com/Bo3cky/AutomationLab.git
```

Placez vous dans le répertoire ```Vagrant-settings```
```bash
cd AutomationLab/Vagrant-settings
```

Puis entrez la commande suivante
```bash
vagrant up
```
Cette commande permet de configurer et de lancer les VM en s'appuyant sur le contenu du fichier vagrantfile.

Le premier lancement sera plus long que les suivants, c'est normal car les images des VM n'ont pas encore été télechargées

Si l'opération se déroule sans problèmes notre laboratoire est prêt a étre utilisé.
Il est composé de 3 machines:
  - 1 node-manager 
  - 2 nodes-clients

Enregistrer les noms d'hôtes des nodes dans le fichier de résolution d'hôtes.

Sur Linux ouvrez un terminal
```bash
sudo su -
sudo echo "192.168.0.10 nodemanager" >> /etc/hosts
sudo echo "192.168.0.11 node1" >> /etc/hosts
sudo echo "192.168.0.12 node2" >> /etc/hosts
```
Sur Windows 10 ouvrez un terminal powershell en tant qu'administrateur
```powershell
echo "192.168.0.10 nodemanager" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.11 node1" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.12 node2" >> 'C:\Windows\System32\drivers\etc\hosts'
```

### Configuration SSH du node-manager

Pour plus de simplicité pour vos tests je vous recommande de générer un clé ssh puis de l'embarqué sur votre agent-ssh

Tout d'abord assurez vous que OpenSSH est installé sur votre machine hôte:
- Pour [Windows](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse)
- Pour [Linux]
```bash
sudo apt-get install openssh-server
```

Conectez vous au node-manager via ssh.

Identifiants:
  - Utilisateur: vagrant
  - Mot de passe: vagrant
```bash
ssh vagrant@nodemanager
```

Ajouter les nodes-clients au fichier hosts.
```bash
sudo su -
sudo echo "192.168.0.11 node1" >> /etc/hosts
sudo echo "192.168.0.12 node2" >> /etc/hosts
```

Générer d'une clé SSH sans passphrase (ou avec comme vous voulez).
```bash
ssh-keygen -f ~/.ssh/vagrant -t rsa -b 4096 -N ""
```

Copier la clé publique sur nos nodes-clients
```bash
ssh-copy-id -i ~/.ssh/vagrant.pub vagrant@node1
ssh-copy-id -i ~/.ssh/vagrant.pub vagrant@node2
```

Démarrage de l'agent ssh (si inactif)
``` bash
eval `ssh-agent`
```

Ajout de la clé privé à l'agent d'authentification SSH
```bash
ssh-add ~/.ssh/exemple
```
Il est maintenant possible de s'authentifier directement sur les nodes-clients sans spécifier de mot de passe

## Installation des packages requis

Sur votre machine hôte copiez le dossier Python-Project sur le node-manager
```bash
scp -rp Python_Project/ vagrant@nodemanger:/home/vagrant
```

Conectez vous au node-manager 
```bash
ssh vagrant@nodemanager
```
Mettre a jour les dépots APT
```bash
sudo apt-get update -y && apt-get upgarde -y
```
Installation d'ansible

```bash
sudo apt-get install ansible -y
```
### Python et pip

Installation et mise a jour de pip
```bash
sudo apt-get install pip -y && pip install --upgrade pip
```
Installation du package [ruamel.yaml](https://github.com/commx/ruamel-yaml)
```bash
pip install ruamel.yaml
```
Ce package servira a modifier des valeurs dans les fichiers YAML lus par ansible
 
### Test de connectivité

Pour vérifier la connectivité et la présence de l'interpréteur python sur les nodes-clients le module ping (module natif d'Ansible) est utilisé. 
```
ansible -i inventaire.ini -m ping all
```
Voici la réponse attendue
```json
node2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
node1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```
l'infrastructure est prête à l'emploi

## Exemples d'utilisation

Deux modes d'utilisation possibles pour l'outil mataf.py

- En ligne de commande
```bash
# Exemple d'utilisation du module de vérification d'intégrité du fichier sshd_config
python3 mataf.py -c -f /etc/ssh/sshd_config
```
- Via le menu intéractif en selectionnant les options affichées
```bash
# Entrer dans le menu depuis la ligne de commande
python3 mataf.py --menumode
```
Puis dirigez vous en selectionnant les numéros correspondants au menu d'automatisation désiré.

## A venir...
Mise en place d'un laboratoire de test avec docker géré par un script bash voir plus en détails [ici](https://github.com/Bo3cky/AutomationLab/blob/main/Docker-Lab-Project)

Implémentation d'un(e) assistant(e) vocal dans le programme mataf.py (lancement de tâches par commande vocal ...)

## Contribution

D'autres fonctionnalités pourront êtres ajoutées comme:
 - Le Scan de l'infrastructure existante et enregistrement des données (nom d'hote, IP, utilisateur... ) dans un inventaire GLPI/JIRA
 - Création/déploiement de certificats  
 
Les possibilités sont multiples et personnalisables la seule limite sera votre imagination.

Si ce projet vous intérresse, soyez libre de proposer des améliorations, de donner des conseils, ou même d'apporter votre contribution à ce programme.

A bientôt Sur GitHub!
