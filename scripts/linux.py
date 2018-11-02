#!/usr/bin/python2
import commands

print "content-type: text/html"

shell=commands.getstatusoutput("rpm -q shellinabox")
	if shell[0]==0:
		
	else:
		commands.getstatusoutput("yum install shellinabox")
commands.getstatusoutput("systemctl restart shellinaboxd")

print "location: ../linux.html"
print
