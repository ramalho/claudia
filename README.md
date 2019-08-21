# Building Claudia


## Project setup

* Python3 (3.7.3)
* Python project
    * `pip install -r requirement.txt`
* Ansible support
    * `pip install ansible` - frequently done globally, so excluded from requirements.txt
    * Install "sshpass": `brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb`


## Automating Raspberry Pi Setup With Ansible

http://www.hietala.org/automating-raspberry-pi-setup-with-ansible.html

## Installing the Unicorn Hat library

Source: https://github.com/pimoroni/unicorn-hat

```
$ sudo apt-get install python3-pip python3-dev
$ sudo pip3 install unicornhat
```

Manual test:

```
$ sudo apt-get install git
$ git clone --depth 1 https://github.com/pimoroni/unicorn-hat.git
$ sudo python3 unicorn-hat/examples/demo

```


## Device map

For the lab at Evolve Coworking in Crested Butte, CO

```
claudia1 - 192.168.86.86
claudia2 - 192.168.86.91
claudia3 - 192.168.86.92
claudia4 - 192.168.86.93
claudia5 - 192.168.86.94
```

