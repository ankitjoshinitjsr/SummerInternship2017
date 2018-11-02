#!/usr/bin/python2

import cgi

print "content-type: text/html"

webip=cgi.FormContent()

fh=open('../Ansible/hosts', 'w')
fh.write("[web]\n")

for i in webip.keys():
        ip=webip[i][0]
        fh.write(ip + "  ansible_ssh_user=root  ansible_ssh_pass=blackhat" + "\n")
fh.close()

print "location: ../workplace.html"
print

