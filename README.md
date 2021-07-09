Création d’un menu interactif  pour l’automatisation de tâches

L’idée principale de ce projet est d'utiliser les différentes technologies à notre disposition pour permettre à l'utilisateur de pouvoir exécuter une/des tâches spécifique sur n’importe quel aspect d’un SI Systèmes, Réseaux, Sécurité


Ce projet a pour but d'automatiser plusieurs tâches via un menu interactif, il  contiendra plusieurs parties :
NetworkAutomation pour la partie d’administration de tâches réseaux
SystemAutomation pour la partie d’administration de tâches systèmes
SecurityAutomation pour la partie d’administration des tâches de sécurité

Pour exécuter ces tâches il suffira de sélectionner la partie pertinente pour vos tests.

Bien sûr il sera tout à fait possible d’étoffer le projet en ajoutant d'autres fonctionnalités comme par exemple la mise en place automatisé d’environnement pour des projets spécifiques via docker et/ou kubernetes.

Voici une vue logique des actions possibles:

![Vue_logique_actions_script](https://user-images.githubusercontent.com/85841056/123432005-30934500-d5ca-11eb-8274-e1dbccfa1c79.png)

Chaque option appellera soit un playbook-ansible soit à un script par exemple “script1.nse” pour nmap, d’autres langages pourront être utilisés sans problèmes.

Une fois la tâche exécutée le résultat sera stocké dans un fichier correspondant.
Par exemple supposons que l’option “Gathering_User_infos”  est sélectionnée, un playbook ansible sera donc exécuté pour récolter des informations concernant les utilisateurs.
Ensuite les "gathering_facts" seront stockés dans le répertoire ./System Directory les données pourront être utilisées pour faire un état des lieux des utilisateurs existants et également reuceuillirleurs attributs.

Les possibilités sont infinies et surtout personnalisables.

Le projet en est à son début je suis ouvert a toutes propositions, conseils, avis d’améliorations sur ce
concept si vous êtes intéressé bien sur.

A bientôt !
