#!/usr/bin/python2
import cgi
import commands

print "content-type: text/html"
print


Bname=cgi.FormContent()['bname'][0]
Cip=cgi.FormContent()['cip'][0]
Cpass=cgi.FormContent()['cpass'][0]

x=commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo ifconfig | grep enp0s".format(Cpass,Cip))
y=x.split('.')
z=y[-1][2:8]


commands.getstatusoutput("sudo touch /naas/daemon.json")
commands.getstatusoutput("sudo chown apache /naas/daemon.json")

x="""{{
    \"bridge\" : \"{0}\"
}}
""".format(Bname)
f1=open('/naas/daemon.json','w')
f1.write(x)
f1.close()

commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /naas/daemon.json root@{1}:/etc/docker/".format(Cpass,Cip))

commands.getstatusoutput(" sudo touch /naas/Dockerfile")
commands.getstatusoutput("sudo chown apache /naas/Dockerfile")
#Creating a Dockerfile with required tools 
y="""FROM centos
RUN yum install net-tools -y
RUN yum install dhclient -y
"""
commands.getstatusoutput("sudo touch /naas/Dockerfile")
commands.getstatusoutput("sudo chown apache /naas/Dockerfile")
f2=open("/naas/Dockerfile",'w')
f2.write(y)
f2.close()

commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mkdir /test".format(Cpass,Cip))

commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /naas/Dockerfile root@{1}:/test/".format(Cpass,Cip))
#Python Script to be run on client side 
a="""#!/usr/bin/python2
import cgi
import commands
commands.getstatusoutput(\"brctl addbr {0}\")\n
commands.getstatusoutput(\"ifconfig {0} 0\")\n
commands.getstatusoutput(\"ifconfig {3} 0\")\n 
commands.getstatusoutput(\"brctl addif {0} {3}\")\n
commands.getstatusoutput(\"killall dhclient\")\n
print commands.getstatusoutput(\"dhclient -v {0}\")\n
""".format(Bname,Iname,Cname,z)

commands.getoutput("sudo touch /naas/naas.py")
commands.getoutput("sudo chown apache /naas/naas.py")
f3=open('/naas/naas.py','w')
f3.write(a)
f3.close()
print commands.getoutput("sudo chmod +x /naas/naas.py")
commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /naas/naas.py root@{1}:/test/".format(Cpass,Cip))

