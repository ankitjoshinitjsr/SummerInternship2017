#!/usr/bin/python2

import cgi
print "content-Type: text/html"

menuCh=cgi.FormContent()['x'][0]

print cgi.FormContent()


if menuCh == "staas":
	print "location: ../staas.html"
	print
elif menuCh =="paas":
	print "location: ../paas.html"
	print
elif menuCh =="caas":
        print "location: ../caas.html"
        print
elif menuCh =="iaas":
        print "location: ../iaas.html"
        print

else:
	print "location: ../menu.html"
	print

