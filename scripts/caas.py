#!/usr/bin/python2

import commands
import cgi

#Combined python CGI and HTML to create a dynamic page
print "content-type: text/html"
print 
print "<b>"
print "<body bgcolor='Aqua'>"
print "<marquee hspace=10 vspace=10 height=40><font><h1> CONTAINER AS A SERVICE</h1></font></marquee>"
print "</b>"
print "<center>"
print "<h2><u>AVAILABLE DOCKER IMAGES</u></h2>"
print "<pre>"
print "<h4>"
print commands.getoutput("sudo docker images")
print "</h4>"
print "</pre>"
print "</center>"
print "<center>"
print "<form action='container.py'>"
print "Select Image Name:"
print "<select name='image'>"
print "<br>"
print "<br>"
z=1
#Display Docker Images
for i in commands.getoutput("sudo docker images").split('\n'):
      if z==1 :
          z+=1
          pass
      else:
          j= i.split()
          print "<option>" + j[0] + ":" + j[1] + "</option>"
print "</select>"
print "<br/>"
print "<br/>"
print "Your Container Name : <input name='cname' />"
print "<input type='submit' value='Start' />"
print "</form>"
print "<h3><u>Launch Multiple Containers</u></h3><br/>"
print "<form action='mcontainer.py'>"
print "Select Image Name:"
print "<select name='image'>"
print "<br>"
print "<br/>"
z=1
for i in commands.getoutput("sudo docker images").split('\n'):
      if z==1 :
          z+=1
          pass
      else:
          j= i.split()
          print "<option>" + j[0] + ":" + j[1] + "</option>"
print "</select>"
print "<br>"
print "<br/>"
print """
      Enter the Number : <input name='n' />
      Unique Id: <input name='id' />
      <input type='submit' value='start' />      
      """
print "</form><br/>"
print """
      <hr />
      <center>
      <h2><u>Create Your Own Image</u></h2>
      <form action="dockerimage.py">
      centos : <input name='os' value='centos' type='radio' /> ubuntu : <input name='os' value='ubuntu' type='radio' /> fedora : <input name='os' value='fedora' type='radio' />
      <br/><br/>
	<b><u>Choose the Services Needed:</u></b><br/>
	<br/>
      SSH Server : <input type='checkbox' name='ssh' value='ssh'/>
      <br/>
      Apache Server : <input type='checkbox' name='web' value='web' />
      <br/>
      Python2 : <input type='checkbox' name='python' value='python'/>
      <br/>
      Net-Tools : <input type='checkbox' name='ntool' value='ntool'/>
      <br/><br/>
      Image Name: <input name="name" /><br/><br/>
      <input type='submit' value='Create Image'>
      </center>
      """  
	
print "</body>"
