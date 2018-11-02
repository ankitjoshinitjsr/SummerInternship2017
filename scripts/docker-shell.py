#!/usr/bin/python2

import cgi
import commands
import Cookie
import os

print "content-type: text/html"
print 


t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
Cname=t["Container_Name"].value
ccmd=cgi.FormContent()['code'][0]
ccmd1=ccmd.split()
print ccmd1
print "<center>"
print "<h3>Input</h3><br>"

print "<h1>"
print ccmd
print "</h1>"
print "<br/>"
print "<h3><font color='red'>Output:</h3></font>"
print "<br/>"
print "<hr/>"
print "<h1>"
print "<pre>"
print "<font color='red'>"
i=0
while i < len(ccmd1):
 print commands.getoutput("sudo docker exec {1} {0}".format(ccmd1[i],Cname))
 i+=1
print "</font>"
print "</pre>"
print "</h1>"
print "</center>"

