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

# Prérequis

Avant de commencer quelques prérequis seront nécéssaires afin de bien comprendre les concepts utilisés dans ce projet

- Etre à l'aise avec la ligne de commande
- Connaître le langage bash
- Connaître le langage python
- Connaître la structure de fichier YAML
- Connaitre les bases du fonctionnement d'Ansible

# Laboratoire de test

L'architechture pour le test de cet outil a été mise en place a l'aide de Vagarant un programme en ligne de commande pour la création, la gestion, et le management, de machines virtuelles.

Ici les liens concernants la mise en place de Vagarant
  - Pour consulter la [documentation](https://www.vagrantup.com/docs)
  - Pour [l'installation](https://www.vagrantup.com/docs/installation) du logiciel Vagrant. 
  - Pour le [téléchargement](https://www.vagrantup.com/downloads) de Vagrant. 

Il faudra également télécharger un hyperviseur de type 2  (ex:Virtualbox, VmwareWorkstation) pour héberger vos VM crées par Vagarant.


