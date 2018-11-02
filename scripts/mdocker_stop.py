#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
 

cName=cgi.FormContent()['y'][0]
removestatus=commands.getstatusoutput("sudo docker stop {0}".format(cName))
if removestatus[0]==0:
   print "location: mcontainer.py"
   print
else:
   print "Error"
   print 
