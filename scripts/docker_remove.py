#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
 

cName=cgi.FormContent()['x'][0]
#Remove Docker From active and sleep state
removestatus=commands.getstatusoutput("sudo docker rm -f {0}".format(cName))
if removestatus[0]==0:
   print "location: docker_manage.py"
   print
else:
   print "Error"
   print 
