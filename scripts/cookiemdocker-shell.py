#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
cName=cgi.FormContent()['z'][0]
print "set-cookie: CNAME={0}".format(cName)
print "location: ../mdocker-shell.html"
print 
