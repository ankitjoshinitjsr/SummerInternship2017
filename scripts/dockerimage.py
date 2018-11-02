#!/usr/bin/python2
import cgi
import commands

print "content-type: text/html"
print 

x=0
y=0
z=0
w=0
a=0
d=cgi.FormContent()
ImageName=cgi.FormContent()['name'][0]
for i in d.keys():
	 if d[i][0]=="ssh":
		x="ssh"
	 elif d[i][0]=="web":
                y="web"
         elif d[i][0]=="ntool":
                z="ntool"
         elif d[i][0] == "python":
                w="python"
         elif d[i][0] == "centos":
                a="centos"
         elif d[i][0] == "fedora":
                a="fedora"
         elif d[i][0] == "ubuntu":
                a="ubuntu"
commands.getoutput("sudo touch /commit/Dockerfile")
commands.getoutput("sudo chown apache /commit/Dockerfile")
if a == "centos":
   commands.getstatusoutput("echo 'FROM centos' | sudo cat >> /commit/Dockerfile")
if x == "ssh":
   commands.getoutput("echo 'RUN yum install openssh -y' | sudo cat >> /commit/Dockerfile")
if y == "web":
   commands.getoutput("echo 'RUN yum install httpd -y' | sudo cat >> /commit/Dockerfile")
if z == "ntool":
   commands.getoutput("echo 'RUN yum install net-tools -y' |sudo cat >> /commit/Dockerfile")
if w == "python":
   commands.getstatusoutput("echo 'RUN yum install python -y' | sudo cat >> /commit/Dockerfile")

commands.getoutput("sudo docker build -t {0} /commit".format(ImageName))
commands.getoutput("sudo rm -rf /commit/Dockerfile")
print "<a href='caas.py'> Go back </a>"
print "<pre>"
print "<h2>"
print commands.getoutput("sudo docker images {0}".format(ImageName))
print "</h2>"










