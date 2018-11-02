#!/usr/bin/python2
import cgi
import commands
import Cookie
import os
print "content-type: text/html"
print 

print cgi.FormContent()
UserName= cgi.FormContent()['user'][0]
UserPassword= cgi.FormContent()['pass'][0]
DriveSize= cgi.FormContent()['size'][0]
print UserPassword,DriveSize
UserStatus=commands.getstatusoutput("sudo useradd "+UserName)
if UserStatus[0] == 0: 
       print "New User Successfully Created"
       
       PasswordStatus = commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo echo {1} | sudo passwd {0} --stdin".format(UserName,UserPassword))
       if PasswordStatus[0]==0:
          print "Pasword Set Successfully.Your Account is ready to use."
          
          commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvcreate --size {0}G --name {1} objectstorage".format(DriveSize,UserName))
          FormatStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkfs.ext4 /dev/objectstorage/{}".format(UserName))
          if FormatStatus[0] == 0:
                print "Format Completed"
                commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkdir -p /cloudssh/{0}".format(UserName))
                MountStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mount /dev/objectstorage/{0} /cloudssh/{0}".format(UserName))
                if MountStatus[0] == 0:
                   print "Mounting of drive created successfully."
                   sshServiceStatus = commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo systemctl restart sshd")
                   if sshServiceStatus[0]== 0:
                      print "SSH server is active."
                      PermissionStatus =commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo chown {0} /cloudssh/{0}".format(UserName))
                      if PermissionStatus[0] == 0:
                         print "User has ben granted access to his folder"
                         DenyOtherUser = commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo chmod 700 /cloudssh/{0}".format(UserName))
                         if DenyOtherUser[0]== 0:
                            print "Other Users cant access your folders."
                         else:
                            print "Other Users may access your folder"
                      else:
                         print "Permissions cannot be given to user "
                   else:
                      print "SSh service failed"

                else:
                   print "dismounting...the drive"
  
       else:
          print "Password could not be created"
else :
       print "User Could not be created"


