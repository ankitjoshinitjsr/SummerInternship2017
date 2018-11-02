#!/usr/bin/python2
import cgi
import commands
import Cookie
import os

print "content-type: text/html"
print 

print cgi.FormContent()
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
Cname=t["CNAME"].value
ccmd=cgi.FormContent()['code'][0]


print "<center>"
print "<h2>Output:</h2>"
print "<br/>"
print "<hr/>"
print "<h1>"
print "<pre>"
print commands.getoutput("sudo docker exec {1} {0}".format(ccmd,Cname))
print "</pre>"
print "</h1>"
print "</center>"

