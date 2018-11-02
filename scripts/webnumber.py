#!/usr/bin/python2

import cgi 

print"content-type: text/html"
print

i=1
webnumber=cgi.FormContent()['webnumber'][0]

print "<form action='/scripts/web1.py'>"
while i<= int(webnumber):
	print "Enter ip {0} <input name='web{0}'/><br/>".format(i)
	i+=1

print"<input type='submit'>"
print"</form>"


