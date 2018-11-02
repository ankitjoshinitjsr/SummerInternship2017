#!/usr/bin/python2
import cgi
import commands

print "content-type: text/html"
print 

Uname=cgi.FormContent()['uname'][0]
date=cgi.FormContent()['date'][0]
Dname=cgi.FormContent()['dname'][0]
x=commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvdisplay /dev/objectstorage/{0} ".format(Dname))
y=x.split()
size=y[-21]
type1=y[-20]
#Create snap using combination of drivename and date on storage server
commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvcreate --size {0}{1} --name {2}{3}.snap -s /dev/objectstorage/{4}".format(size,type1,Uname,date,Dname))
print "<pre>"
print commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvdisplay /dev/objectstorage/{0}{1}.snap".format(Uname,date))
commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkdir -p /snap/{0}{1}.snap".format(Uname,date))
commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mount /dev/objectstorage/{0}{1}.snap /snap/{0}{1}.snap".format(Uname,date))
commands.getstatusoutput("echo '/snap/{0}{1}.snap  *(rw,no_root_squash)' | sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo 'cat >> /etc/exports'".format(Uname,date))
print "</pre>"
