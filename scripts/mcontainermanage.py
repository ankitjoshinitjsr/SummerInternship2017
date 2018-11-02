#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print 

print "<center>"
print "<h1>Manage The Containers</h1>"
print "<br/><hr/><br/>"

print"""
<script>
function lw(mycname)
{
document.location='mdocker_remove.py?x='+mycname;

}
function lw2(mycname2)
{
document.location='mdocker_stop.py?y='+mycname2;

}
function lw3(mycname3)
{
document.location='cookiemdocker-shell.py?z='+mycname3;

}
</script>
"""

print "<table border='5'>"
print "<tr><th>Image Name</th><th>Container Name</th><th>Status</th><th>IP Address</th><th>Stop</th><th>Shell</th><th>Remove</th></tr>"

z=1
for i in commands.getoutput("sudo docker ps ").split('\n'):
    if z == 1:
       z+=1
       pass
    else:
       j=i.split()
       cStatus=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
       ipstatus=commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(j[-1]))
       print "<tr><td> " + j[1] + "' </td><td> " + j[-1] + " </td><td>" + cStatus + "</td><td>" + ipstatus[1].strip('"') + "</td><td> <input value='" +j[-1]+"' type='button' onclick=lw2(this.value) /> </td><td> <input value='" +j[-1]+"' type='button' onclick=lw3(this.value) /> </td><td> <input value='" + j[-1] + "' type='button' onclick=lw(this.value) /> </td></tr>"

print "</table>"
print "</center>"

