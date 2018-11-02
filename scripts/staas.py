#!/usr/bin/python2

import cgi

print "content-Type: text/html"

menuCh=cgi.FormContent()['storage'][0]

if menuCh == "objectstorage":
        print "location: ../storageoption.html"
        print
elif menuCh == "blockstorage":
        print "location: ../blockstorage.html"
        print


else:
	print "wrong choice"

