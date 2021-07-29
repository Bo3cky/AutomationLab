# PRESENTATION
The main idea of this project is to use the different technologies at our disposal to enable the administrator to automate one or more specific tasks on different aspects of an IS.


The program [mataf.py](https://github.com/Bo3cky/AutomationLab/blob/main/Python_Project/mataf.py) 3 parts:

- NetworkAutomation for the network task administration part
- SystemAutomation for the system task administration part
- SecurityAutomation for the administration part of security tasks

This image does not represent the options currently implemented in the tool.

Here is a logical view of possible actions:


![IMAGE1](https://github.com/Bo3cky/AutomationLab/blob/main/Images/Vue_logique_actions_script.png)

Each of the options relies on several processes (playbook-ansible, bash script) to perform a predefined task list. Other mechanisms or programming languages can be implemented.Once the task is executed the result will be stored in a dedicated directory.

### Knowledge
Before starting some prerequisites will be necessary to fully understand the concepts used in this project

- Knowledge of bash language
- Know the python language
- Know the YAML file structure
- Know the basics of how Ansible works
- Have administrator(root) rights on the machine used
- Being comfortable with the command line is a plus

### Materiel
Here is the recommended hardware configuration for the test lab installation

- RAM: 8GB
- CPU: (4cores/8threads)
- Storage: HDD/SDD
 
## Test Lab

The architecture set up for the mataf.py program test was built using the Vagrant tool, a command-line program that allows the creation, management, and management of virtual machines.

Here are the links concerning the documentation and installation of Vagrant
- To consult the [documentation](https://www.vagrantup.com/docs)
- For [installation](https://www.vagrantup.com/docs/installation) of the Vagrant software.
- For [download](https://www.vagrantup.com/downloads) from Vagrant.

You will also need to download a type 2 hypervisor (e.g., Virtualbox, VmwareWorkstation) to host VMs created by Vagrant.
- To install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- To install [Vmware Workstation](https://www.vmware.com/fr/products/workstation-player.html)



## Configuration

For upload this repository:
```bash
git clone https://github.com/Bo3cky/AutomationLab.git
```

Place yourself in this directory ```Vagrant-settings```
```bash
cd AutomationLab/Vagrant-settings
```

Then enter the following command
```bash
vagrant up
```
This command allows you to configure and launch VMs based on the contents of the vagrantfile.

The first launch will be longer than the following ones, this is normal because the VM images have not yet been uploaded

If the operation goes smoothly our laboratory is ready to be used.
It is composed of 3 machines:
  - 1 node-manager 
  - 2 client nodes

Save the host names of the nodes in the host resolution file.

On Linux open a terminal
```bash
sudo su -
sudo echo "192.168.0.10 nodemanager" >> /etc/hosts
sudo echo "192.168.0.11 node1" >> /etc/hosts
sudo echo "192.168.0.12 node2" >> /etc/hosts
```
On Windows 10 open a powershell terminal as administrator
```powershell
echo "192.168.0.10 nodemanager" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.11 node1" >> 'C:\Windows\System32\drivers\etc\hosts'
echo "192.168.0.12 node2" >> 'C:\Windows\System32\drivers\etc\hosts'
```

### SSH configuration on node-manager

For simplicity for your tests I recommend generating an ssh key then embedded on your ssh-agent.
Or create a file named config in your ~/.ssh/ folder containing connections parameters.

Tout d'abord assurez vous que OpenSSH est installé sur votre machine hôte:
- For [Windows](https://docs.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_install_firstuse)
- For [Linux]
```bash
sudo apt-get install openssh-server
```

Connect to the node-manager via ssh

Credentials:
  - User: vagrant
  - Passowrd: vagrant
```bash
ssh vagrant@nodemanager
```

Add the clients on the host file.
```bash
sudo su -
sudo echo "192.168.0.11 node1" >> /etc/hosts
sudo echo "192.168.0.12 node2" >> /etc/hosts
```

Generate a ssh key without a passphrasse (or with as you want).
```bash
ssh-keygen -f ~/.ssh/vagrant -t rsa -b 4096 -N ""
```

Copy the public key on the clients
```bash
ssh-copy-id -i ~/.ssh/vagrant.pub vagrant@node1
ssh-copy-id -i ~/.ssh/vagrant.pub vagrant@node2
```

ssh agent startup (if inactive)
``` bash
eval `ssh-agent`
```
Adding the Private Key to the SSH Authentication Agent
```bash
ssh-add ~/.ssh/vagrant
```
It is now possible to authenticate directly on customers without specifying a password

## Install requierd packages

On your host machine copy the folder Python-Project on the node-manager
```bash
scp -rp Python_Project/ vagrant@nodemanger:/home/vagrant
```

Connect to the node-manager 
```bash
ssh vagrant@nodemanager
```
Update APT repositories
```bash
sudo apt-get update -y && apt-get upgarde -y
```

Installation of ansible
```bash
sudo apt-get install ansible -y
```
### Python and pip

Installation and updating of pip
```bash
sudo apt-get install pip -y && pip install --upgrade pip
```
Package installation [ruamel.yaml](https://github.com/commx/ruamel-yaml)
```bash
pip install ruamel.yaml
```
This package will be used to change values in YAML files read by ansible
 
### Test de connectivité

To check connectivity and the presence of the python interpreter on client nodes the ping module (native Ansible module) is used. 
```
ansible -i inventaire.ini -m ping all
```
Here is the expected answer
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
Our infrastructure is ready for use

## Usage 

Two possible modes of use for the mataf.py tool

- Command line 
```bash
# Exemple d'utilisation du module de vérification d'intégrité du fichier sshd_config
python3 mataf.py -c -f /etc/ssh/sshd_config
```
- Via the Interest menu by selecting the options displayed
```bash
# Entrer dans le menu depuis la ligne de commande
python3 mataf.py --menumode
```
Then navigate by selecting the corresponding numbers from the desired automation menu.

## Coming soon...
Setting up a test lab with docker managed by a bash script.
More details [here](https://github.com/Bo3cky/AutomationLab/blob/main/Docker-Lab-Project)

Implementation of voice assistance in the mataf.py program (launch and scheduling of tasks by voice commands, etc.)

## Contribute to MATAF

Other features may be added such as:
- Mapping of the existing infrastructure and recording of data (hostname, IP, user...) in a GLPI/JIRA inventory
- Creation/deployment of security certificates

The possibilities are multiple and customizable the only limit will be your imagination.

If you are interested in this project, be free to suggest improvements, provide advice, or even make your contribution to this program.

See you soon on GitHub!
