#!/usr/bin/python2

import commands
import cgi 


print"Content-Type: text/html"
print

driveName=cgi.FormContent()['drive'][0] 
umountStatus=commands.getstatusoutput("umount {}".format(driveName)
commands.getoutput("umountStatus")

"""
if umountStatus[0] == 0:
	print "your drive unmounted successfully"
else:
	print "drive unmount unsuccessfull"

"""
