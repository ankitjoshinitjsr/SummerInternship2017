#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

#input

name=cgi.FormContent()['name'][0]
ostype=cgi.FormContent()['ostype'][0]
osvariant=cgi.FormContent()['osvariant'][0]
memory=cgi.FormContent()['memory'][0]
cpu=cgi.FormContent()['cpu'][0]
port=cgi.FormContent()['port'][0]

serverip=cgi.FormContent()['serverip'][0]
serverpass=cgi.FormContent()['serverpass'][0]

clientip=cgi.FormContent()['clientip'][0]
clientpass=cgi.FormContent()['clientpass'][0]

#software installation
status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q qemu-kvm".format(serverpass,serverip))
if status[0]!=0:
    status1=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install qemu-kvm -y".format(serverpass,serverip))
    status2=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install virt-manager -y".format(serverpass,serverip))    
    if status2[0]!=0 or status1[0]!=0:
       print "Failed to install software in server side"
       exit()
else:
    print "software already installed"

print"<br />"

status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q virt-install".format(serverpass,serverip))
if status[0]==0:
    print "virt-install already installed" 
else:
    status1=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install virt-install -y".format(serverpass,serverip))
    if status1[0]!=0:
       exit()

print"<br />"
#service start
status=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no -l root {} systemctl restart libvirtd".format(serverpass,serverip))
#configuration

status=commands.getstatusoutput("sshpass -p {6} ssh -o stricthostkeychecking=no -l root {7} sudo virt-install --name {0} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type {1} --os-variant {2} --memory {3} --vcpus {4} --disk /var/lib/libvirt/images/{0}.qcow2,size=7 --graphics vnc,listen=0.0.0.0,port={5} --noautoconsole".format(name,ostype,osvariant,memory,cpu,port,serverpass,serverip))

if status[0]==0:
    print "Virtual OS successfully started"
else:
    print "Virtual OS failed to start"
    exit()
#client side

print"<br />"
#software installation
status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q tigervnc".format(clientpass,clientip))
if status[0]!=0:
    status1=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install tigervnc -y".format(clientpass,clientip)) 
    if status1[0]!=0:
       print "Failed to install tigervnc in client side"
       exit()
else:
    print "Tiger-vnc already installed"
#starting 


print"<br />"

commands.getstatusoutput("sudo chown apache /pk/upload/iaasuser.py")
fil=open("/pk/upload/iaasuser.py",'w')
fil.write("#!/usr/bin/python2\nimport commands\ncommands.getstatusoutput(\"sudo vncviewer {}:{}\")".format(serverip,port))     
fil.close()

clientStatus=commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /pk/upload/iaasuser.py root@{1}:/root/Desktop".format(clientpass,clientip))


if clientStatus[0]==0:
    print "Os started on client OS"
else:
    print "OS failed to launch on Client OS"

print"<br />"
