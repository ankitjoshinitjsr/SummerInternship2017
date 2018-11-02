#!/usr/bin/python2
import commands
import cgi
import Cookie
import os
print "content-type: text/html"
print

DriveName = cgi.FormContent()['drive1'][0]
Resize = cgi.FormContent()['size'][0]
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
UserName=t["x"].value
#Checking whether Drive Exist or Not
Exist=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo df -h | grep {}$".format(DriveName))
#If Drive Exist Extend the logical Volume
if Exist[0] == 0:
   print "Found!!"
   Exlv = commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvextend --size +{}G /dev/objectstorage/{}".format(Resize,DriveName))
   if Exlv[0] == 0:
      print "LV extended"
      Status=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo resize2fs /dev/objectstorage/{}".format(DriveName))
      print "Your Drive is Ready to Use"

