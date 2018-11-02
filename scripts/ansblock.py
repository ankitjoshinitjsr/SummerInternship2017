#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

user=cgi.FormContent()['user'][0]
paswd=cgi.FormContent()['paswd'][0]
ip=cgi.FormContent()['ip'][0]
vg=cgi.FormContent()['vg'][0]
clientpass=cgi.FormContent()['clientpass'][0]
clientip=cgi.FormContent()['clientip'][0]
size=cgi.FormContent()['size'][0]
print user

write="""[storageserver]
{0}   ansible_ssh_user=root  ansible_ssh_pass={1}

[webserver]
192.168.43.150  ansible_ssh_user=root  ansible_ssh_pass=blackhat

[clientserver]
{2}   ansible_ssh_user=root  ansible_ssh_pass={3}
""".format(ip,paswd,clientip,clientpass)
print write
print commands.getstatusoutput("sudo touch /webcontent/Ansible/hosts")
print commands.getstatusoutput("sudo chown apache /webcontent/Ansible/hosts")

f2=open("/webcontent/Ansible/hosts",'w')
f2.write(write)
f2.close()


#print user
#print paswd

write1="""---
- hosts: storageserver
  tasks:

        - package:
                         name: "scsi-target-utils.x86_64"
                         state: present

        - file:
                         state: directory
                         path: "/gbs"

        - fetch:
                         src: "/etc/tgt/targets.conf"
                         dest: "/gbs/"
                         flat: yes

        - lvol:
                         vg: "{0}"
                         lv: "{1}"
                         size: "{2}"
                          
- hosts: webserver
  tasks:
        - file:
                         path: "/gbs/targets.conf"
                         owner: "apache"

        - blockinfile:
                         path: "/gbs/targets.conf"
                         block:  |
                           <target {1}>
                               backing-store /dev/{0}/{1}
                           </target>

- hosts: storageserver
  tasks:
        - copy:
                         src: "/gbs/targets.conf"
                         dest: "/etc/tgt/targets.conf"



        - service:
                         name: "tgtd"
                         state: restarted

- hosts: clientserver
  tasks:
        - open_iscsi:
                         show_nodes: yes
                         discover: yes
                         portal: {3}
                         login: yes
                         target: {1}
""".format(vg,user,size,ip)
commands.getstatusoutput("sudo touch /webcontent/Ansible/part1.yml")
commands.getstatusoutput("sudo chown apache /webcontent/Ansible/part1.yml")
f1=open("/webcontent/Ansible/part1.yml",'w')
f1.write(write1)
f1.close()


print commands.getstatusoutput("sudo ansible-playbook ../Ansible/part1.yml -i ../Ansible/hosts")

print "Allocated"
