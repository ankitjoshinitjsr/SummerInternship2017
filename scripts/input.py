#!/usr/bin/python2

import cgi

print "content-type: text/html"
print


count=cgi.FormContent()['c'][0]

print count
i=1

print "<form action=/scripts/input.py method='post'>"
while i<=5:
	print " Enter your ip address{0} <input type='text' name='n{0}' />".format(i)
	print "<br />"
	i=i+1
print "<input type='submit' />"
print "</form>"
