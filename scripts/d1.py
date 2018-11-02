#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print 


Password = cgi.FormContent()['pass'][0]
Ipaddress = cgi.FormContent()['ip'][0]
Dirname = cgi.FormContent()['dir'][0]
DirStatus=commands.getstatusoutput("sshpass -p {} ssh -o stricthostkeychecking=no -l root {} sudo mkdir /{}".format(Password,Ipaddress,Dirname))
if DirStatus[0] == 0:
   print "Folder created successfully"
   ConfStatus=commands.getstatusoutput("sshpass -p {} ssh -o stricthostkeychecking=no -l root {} sudo touch /etc/httpd/conf.d/deploy.conf".format(Password,Ipaddress))
   if ConfStatus[0] == 0:
      print "Configuration File Created"
      port= cgi.FormContent()['port'][0]
      PortStatus=commands.getstatusoutput("echo 'listen {0}' | sshpass -p {1} ssh -o stricthostkeychecking=no -l root {2} sudo 'cat >> /etc/httpd/conf.d/deploy.conf'".format(port,Password,Ipaddress))
      if PortStatus[0] == 0:
         print "New port Added"
         commands.getoutput("echo '<Directory /{0}>' | sshpass -p {1} ssh -o stricthostkeychecking=no -l root {2} sudo 'cat >> /etc/httpd/conf.d/deploy.conf'".format(Dirname,Password,Ipaddress))
         commands.getoutput("echo 'require all granted' | sshpass -p {0} ssh -o        stricthostkeychecking=no -l root {1} sudo 'cat >> /etc/httpd/conf.d/deploy.conf'".format(Password,Ipaddress))
         commands.getoutput("echo '</Directory>' | sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo 'cat >> /etc/httpd/conf.d/deploy.conf'".format(Password,Ipaddress))
         commands.getoutput("echo 'Documentroot /{0}' | sshpass -p {1} ssh -o stricthostkeychecking=no -l root {2} sudo 'cat >> /etc/httpd/conf.d/deploy.conf'".format(Dirname,Password,Ipaddress))
         commands.getoutput("sshpass -p {} ssh -o stricthostkeychecking=no -l root {} sudo systemctl retstart httpd ".format(Password,Ipaddress))
      else :
         print "port could not be added"
   else :
      print "Configuration File could not be created"
else:
   print "Retry....."
print "No error"






