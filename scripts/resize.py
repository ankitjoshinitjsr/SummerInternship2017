#!/usr/bin/python2

import cgi
print "content-Type: text/html"

menuCh=cgi.FormContent()['resize'][0]

print cgi.FormContent()


if menuCh == "increase":
        print "location: /resize_nfs.py"
        print
elif menuCh =="decrease":
        print "location: /resize_nfs1.py"
        print
