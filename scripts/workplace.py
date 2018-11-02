#!/usr/bin/python2

import cgi

print "Content-Type: text/html"


menuch=cgi.FormContent()['service'][0]

if menuch == "webserver":
        print "location: ../scripts/finalserver.py"
        print

elif menuch =="":
        print "location: ../paas.html"
        print
elif menuch =="caas":
        print "location: ../caas.html"
        print
elif menuch =="iaas":
        print "location: ../iaas.html"
        print

else:
	print "error" 
        print 
