# Ansible setup


1. Activate your target virtual env
1. `pip install ansible`
1. Install "sshpass": `brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb`

Note: Normally, you deploy ssh keys to each ansible target. In our case, we want to support frequent drive reformatting, so we will install sshpass to allow Ansible to use plain ssh user / password.


## Use

If the pi's IPs have changed, gather all raspberry pi IPs and update `ansible/inventory.yaml`.

Every time we run ansible, we include the inventory file. Why? Ansible will look in `/etc/ansible/hosts` for this file, but we want to keep it in the GitHub repo.

There are two ways to run Ansible - run a playbook, or run a module providing params.

```
# Run a playbook
ansible-playbook -i inventory.yaml

# Run a playbook for a single pi
ansible-playbook -i inventory.yaml -l claudia_1 

# Run a module in immediate mode
ansible -i inventory.yaml
```

A successful script run looks like:

```
ᐅ ansible-playbook -i inventory.yaml -l claudia_1  install_python.yaml

PLAY [Install python] ******************************************************************************************************************************************************

TASK [Install my ssh keys on the pi's] *************************************************************************************************************************************
 [WARNING]: Platform linux on host claudia_1 is using the discovered Python interpreter at /usr/bin/python, but future installation of another Python interpreter could
change this. See https://docs.ansible.com/ansible/2.8/reference_appendices/interpreter_discovery.html for more information.

changed: [claudia_1]

PLAY RECAP *****************************************************************************************************************************************************************
claudia_1                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Initial setup

If pi's have been reset, or joined a new network, run a network scan and identify the new IPs, set them in `./ansible/inventory.yaml`

Use ansible to install all software: `ansible-playbook -i inventory.yaml 0.setup.yaml`

You can verify that inventory claudia_1 is assigned the correct IP address with:

```
ansible-playbook -i inventory.yaml -l claudia_1 1.identify_nodes.yaml
```


## Troubleshooting and other tips

### How to gather all raspberry pi OS information

Run this command: ` ansible -i inventory.yaml all -m gather_facts --tree ./facts`

Ansible gathers all information it can from all Raspberrys, will display on screen, and also save json in `./ansible/facts`. 



