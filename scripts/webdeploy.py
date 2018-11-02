#!/usr/bin/python2

import cgi
import commands

print "content-type:  text/html"
print


softwareName=cgi.FormContent()['sname'][0]

myansible="""
---
- hosts: web
  tasks:
    - package:
       name: {}
       state: present
""".format(softwareName)


fh=open('../Ansible/web.yaml', 'w')
fh.write(myansible)
fh.close()

print commands.getstatusoutput("sudo ansible-playbook  ../Ansible/web.yaml -i ../Ansible/hosts")



