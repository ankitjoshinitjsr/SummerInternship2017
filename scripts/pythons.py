#!/usr/bin/python2

import cgi
import commands
import os 


print "content-type: text/html"
print

x=cgi.FormContent()['textarea']
print x


print commands.getstatusoutput("sudo touch /webcontent/scripts/example.py")
print commands.getstatusoutput("sudo chown apache /webcontent/scripts/example.py")

fh=open('/webcontent/scripts/example.py', 'w')
fh.write(x)
fh.close()

print commands.getoutput("cat /webcontent/scripts/example.py")
"""
out=commands.getstatusoutput("python /webcontent/scripts/example.py")
print out

"""





