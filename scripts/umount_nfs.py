#!/usr/bin/python2

import commands
import cgi 
import Cookie
import os

print"Content-Type: text/html"
print

driveName=cgi.FormContent()['drive2'][0] 
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
UserName=t["x"].value
umountStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo umount -l /cloud/{0}/{1}".format(UserName,driveName)
if umountStatus[0] == 0:
	print "your drive unmounted successfully"
else:
	print "drive unmount unsuccessfull"

