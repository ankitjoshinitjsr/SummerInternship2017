#!/usr/bin/python2
import cgi
import commands
print "content-type: text/html"
print 

print cgi.FormContent()['f'][0]


