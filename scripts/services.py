#!/usr/bin/python2

import cgi
print "content-type: text/html"

menuCh=cgi.FormContent()['service'][0]

if menuCh == "staas":
	print "location: ../staas.html"
	print
elif menuCh =="paas":
	print "location: ../paas.html"
	print
elif menuCh =="caas":
        print "location: caas.py"
        print
elif menuCh =="iaas":
        print "location: ../iaas.html"
        print

