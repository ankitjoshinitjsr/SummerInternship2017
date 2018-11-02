#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

Os=cgi.FormContent()['image'][0]
Cname=cgi.FormContent()['cname'][0]
print "set-cookie: Container_Name={0}".format(Cname)
print
print Os,Cname
print """
      <center>
      <h1>CloudHat Web Services</h1>
      <br/>
      <hr/>
      <h2>Container is ready to use</h2>
      <br/>
      <hr/>
     """
if commands.getstatusoutput("sudo docker inspect {0}".format(Cname))[0] == 0:
   print "{0}: this container name already exists".format(Cname)
   print "<a href='caas.py'> Click Here to Go Back</a>"
else:
   commands.getstatusoutput("sudo systemctl restart docker")
   commands.getstatusoutput("sudo docker run -dit --name={0}  {1}".format(Cname,Os))                                      
   ipstatus=commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(Cname))
   print "<center>"
   print "IP address of Your Container is : "
   print ipstatus[1]
   print "<a href='../docker-shell.html'>Online Shell</a>"
   print "<br/><br/>"
   print "</center>"
print "<h2>Manage Running Containers</h2>"
print "<a href='docker_manage.py'> Click here to Manage Your Containers</a>"

































