# LOGS ANALYSIS

## INTRODUCTION ...

In this project we have built an informative summary from logs. These logs are allocated in a __POSTGRESQL__ DataBase and all the logic is stored in specific sql depending on the information we are searching on. In addition, we use a python script to recover and show in screen all the results ...

## HOW TO ...

First of all, you need to install *vagrant*: https://www.vagrantup.com/

Once, this is done, just type following:

```language
vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'bento/ubuntu-16.04-i386' is up to date...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 8000 (guest) => 8000 (host) (adapter 1)
    default: 8080 (guest) => 8080 (host) (adapter 1)
    default: 5000 (guest) => 5000 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => C:/Users/bluetab/Projects/INTRO/BACK/PJT1/fullstack-nanodegree-vm/vagrant
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
vagrant ssh
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-75-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.


The shared directory is located at /vagrant
To access your shared files: cd /vagrant
Last login: Mon Jul  3 12:52:06 2017 from 10.0.2.2
vagrant@vagrant:~$
```

## RUN IT ...

You just have to execute: 

```language
cd /vagrant/news
psql -d news -f newsdata.sql
python news.py
```

and the output will appear

## SCREEN OUTPUT ...

```language
________________________________________________________________________________

First Question
________________________________________________________________________________

Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views
________________________________________________________________________________

Second Question
________________________________________________________________________________

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
________________________________________________________________________________

Third Question
________________________________________________________________________________

2016-07-17 2.26%
________________________________________________________________________________

```

## JUST 2 FINISH ...

In order to have code more legible, a *sqls* directory has been created to allocate the different questions to our news database ... I hope you like it!!!