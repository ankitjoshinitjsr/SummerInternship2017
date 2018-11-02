#!/usr/bin/python2
import commands
import cgi
print "content-Type: text/html"
print""


print"saumya"
print"<hi>myprojeect cmd: </h1>"
cmd=cgi.FormContent()['x'][0]

print "<pre>"
print commands.getoutput("sudo " + cmd)
print "</pre>"

