#!/usr/bin/python2

import cgi
import commands
import Cookie
import os
print "content-type: text/html"
print 

#input from HTML page
DriveName = cgi.FormContent()['drive'][0]
Size = cgi.FormContent()['size'][0]
Cip = cgi.FormContent()['ip'][0]
Pass = cgi.FormContent()['pass'][0]
print DriveName 
#using cookie to maintain username
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
UserName=t["x"].value
#creating logical volume
LvStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvcreate --size {0}G --name {1} objectstorage".format(Size,DriveName))

if LvStatus[0] == 0:
   FormatStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkfs.ext4 /dev/objectstorage/{0} ".format(DriveName))
   if FormatStatus[0] == 0:
      commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkdir -p /cloud/{0}/{1} ".format(UserName,DriveName))
#Mounting logical volume on storage server side
      MountStatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mount /dev/objectstorage/{0} /cloud/{1}/{0}".format(DriveName,UserName))

      if MountStatus[0] == 0:
         ShareStatus=commands.getstatusoutput("echo '/cloud/{0}/{1}  *(rw,no_root_squash)' | sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo 'cat >> /etc/exports'".format(UserName,DriveName))
         if ShareStatus[0] == 0:
            PermMount=commands.getstatusoutput("sshpass -p ucantcme sudo scp root@192.168.43.46:/etc/fstab /fs/")
            commands.getoutput("sudo chown apache /fs/fstab")
            s="/dev/objectstorage/{0} /cloud/{1}/{0} ext4 defaults 1 2".format(DriveName,UserName)
            fs=open('/fs/fstab','a')
            fs.write(s+'\n')
            fs.close()
    
            commands.getstatusoutput("sshpass -p ucantcme sudo scp /fs/fstab root@192.168.43.46:/etc/")
#Restarting NFS service at storage server            
            commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo systemctl restart nfs")
#Mounting Drive on client side
            commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mkdir /media/{2}".format(Pass,Cip,DriveName))
            commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mount 192.168.43.46:/cloud/{2}/{3} /media/{3}".format(Pass,Cip,UserName,DriveName))
            print "<br/>"
            print "You Have been Successfully Alloted {}GB space.Check on Your Desktop.".format(Size)
            print "<br/>"
            print "Thanks For Using Our Service"
            print "<br/>"
            print "Check Out our Other Services Also."
         else :
            print "Failed status 4...Please Contact Support Team."
      else:
         print "Failed status 3...Please Contact Support Team."
   else: 
         print "Failed status 2...Please Contact Support Team."
else:
   print "Failed status 1...Please Contact Support Team."
     
=