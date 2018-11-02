#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"


UserName = cgi.FormContent()['UserName'][0]
Password = cgi.FormContent()['password'][0]

auser="cloudhat"
apass="cloudhat"

if UserName == auser and Password == apass :
   print "set-cookie: x={0}".format(UserName)
   print "set-cookie: y={0}".format(Password)
   print "location: ../newpage.html"
   print 
else:
   print "Username or Password did not match."
