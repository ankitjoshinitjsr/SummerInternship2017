#!/usr/bin/python2
import cgi
import commands
print "content-Type: text/html"
print

ipaddress=cgi.FormContent()['ip'][0]
packagename=cgi.FormContent()['rpm'][0]
status1=commands.getstatusoutput("sshpass -p redhat1 ssh -o stricthostkeychecking=no -l root {0} sudo yum install {1} -y".format(ipaddress,packagename))
if status1[0]==0:
	print"software installed successfully "
else:
	print"not installed"
