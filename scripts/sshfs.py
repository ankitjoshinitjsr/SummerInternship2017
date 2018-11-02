#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
print

#input from HTML pages
DriveSize=cgi.FormContent()['size'][0]
Cip=cgi.FormContent()['cip'][0]
Sip=cgi.FormContent()['sip'][0]
Spass=cgi.FormContent()['spass'][0]
Cpassword=cgi.FormContent()['cpass'][0]
Vg=cgi.FormContent()['vg'][0]
UserName=cgi.FormContent()['user'][0]
#creating user at server side
UserStatus=commands.getstatusoutput("sshpass -p {2} ssh -o stricthostkeychecking=no -l root {0} sudo useradd {1}".format(Sip,UserName,Spass))
if UserStatus[0] == 0: 
       print "New User Successfully Created"
       PasswordStatus = commands.getstatusoutput("echo '{1}' | sshpass -p {2} ssh -o stricthostkeychecking=no -l root {3} sudo passwd {0} --stdin".format(UserName,Cpassword,Spass,Sip))
       print PasswordStatus
       if PasswordStatus[0]==0:
          print "Pasword Set Successfully.Your Account is ready to use."
#making entry for client and server to be configured using Ansible
y="""[web]
{0} ansible_ssh_user=root ansible_ssh_pass={1}
[client]
{2} ansible_ssh_user=root ansible_ssh_pass={3}
""".format(Sip,Spass,Cip,Cpassword)

commands.getstatusoutput("sudo mkdir /webcontent/ansible/hosts")
commands.getstatusoutput("sudo chown apache /webcontent/ansible/hosts")
f3=open('/webcontent/ansible/hosts','w')
f3.write(y)
f3.close()

x="""---
- hosts: web
  tasks:
    
     - package:
         name: "sshpass-1.06-1.el7.x86_64"
         state: present
     
     - lvol:
         vg: "{0}"
         lv: "{1}"
         size: "{2}"

     - file:
         state: directory
         path: "/sshcloud/{1}"
         owner: {1}
         mode: 0700
  
     - filesystem:
         fstype: ext4
         dev: "/dev/{0}/{1}"
 
     - mount:
         path: "/sshcloud/{1}"
         src: "/dev/{0}/{1}"
         fstype: ext4      
         state: mounted  
     - service:
         name: "sshd"
         state: restarted
- hosts: client
  tasks:
     - package:
         name: "fuse-sshfs-2.5-1.el7.x86_64"
         state: present
     - file:
         state: directory
         path: "/media/{1}"
     - package:
         name: "sshpass-1.06-1.el7.x86_64"
         state: present 
""".format(Vg,UserName,DriveSize)
f1=open("/webcontent/scripts/ansshfs.yml",'w')
f1.write(x)
f1.close()
print commands.getstatusoutput("sudo ansible-playbook ansshfs.yml -i /webcontent/ansible/hosts")
commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sshpass -p {4} sshfs root@{3}:/sshcloud/{2} /media/{2}".format(Cpassword,Cip,UserName,Sip,Spass))
print "Successfully created"
