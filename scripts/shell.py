#!/usr/bin/python2

import cgi
import commands


print"content-type: text/html"
print

ccmd=cgi.FormContent()['code'][0]


commands.getstatusoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.150 sudo docker start web1")
j=commands.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.150 sudo docker exec web1 {0}".format(ccmd))
x= j.split('.')
print x[-1]
commands.getstatusoutput("sshpass -p blackhat -o stricthostkeychecking=no -l root 192.168.43.150 sudo docker stop -f web1")


