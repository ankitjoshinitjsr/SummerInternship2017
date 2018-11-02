#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"

Count=cgi.FormContent()['n'][0]
Image=cgi.FormContent()['image'][0]
Id=cgi.FormContent()['id'][0]

k=0
#Runs all the containers
while k<int(Count):
	commands.getoutput("sudo docker run -dit --name={1}{2}.centos {0}".format(Image,k,Id))
	k+=1
print "location: mcontainermanage.py"
print

