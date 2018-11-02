#!/usr/bin/python2

import cgi
import commands

print "content-Type: text/html"

langCh=cgi.FormContent()['paas'][0]
if langCh == "python":
        print "location: ../pythonform.html"
        print
elif langCh == "linux":
	print "location: ../linux.html"
	print
elif langCh =="docker":
        print "location: ../shell.html"
        print
elif langCh =="html":
        print "location: ../iaas.html"
        print
else:
	print "wrong choice"

