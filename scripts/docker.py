#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print 


print cgi.FormContent()

imageName=cgi.FormContent()['image'][0]
OSname=cgi.FormContent()['os'][0]
commands.getstatusoutput("sudo systemctl restart docker")
commands.getstatusoutput("sudo docker run -dit --name={0}.centos {1}".format(OSname,imageName))

ipstatus=commands.getstatusoutput("sudo docker inspect {0}.centos | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(OSname))

print ipstatus[1]
print "<a href='../docker-shell.html'>link</a>"

