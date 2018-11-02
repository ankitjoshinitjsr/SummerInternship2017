#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
print 

DriveName = cgi.FormContent()['drive'][0]
Password = cgi.FormContent()['pass'][0]
DriveSize= cgi.FormContent()['size'][0]
clientIp = cgi.FormContent()['sip'][0]
Lvstatus=commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo lvcreate --size {0}G --name {1} blockstorage".format(DriveSize,DriveName))
if Lvstatus[0]==0:
   commands.getoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo mkfs.ext4 /dev/blockstorage/{0}".format(DriveName))
   commands.getoutput("sshpass -p ucantcme sudo scp root@192.168.43.46:/etc/tgt/targets.conf /fs/")
   commands.getoutput("sudo chown apache /fs/targets.conf")
   commands.getoutput("echo '<target {}>' | sudo cat >> /fs/targets.conf".format(DriveName))
   commands.getoutput("echo 'backing-store /dev/blockstorage/{0}' | sudo cat >> /fs/targets.conf".format(DriveName))
   commands.getoutput("echo '</target>' | sudo cat >> /fs/targets.conf")
   commands.getoutput("sshpass -p ucantcme sudo scp /fs/targets.conf root@192.168.43.46:/etc/tgt/")
   commands.getstatusoutput("sshpass -p ucantcme ssh -o stricthostkeychecking=no -l root 192.168.43.46 sudo systemctl restart tgtd")
   commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.46 --discover".format(Password,clientIp))
   Status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo iscsiadm --mode node --targetname {2} --portal 192.168.43.46:3260 --login".format(Password,clientIp,DriveName))
   if Status[0]==0:
      print "You have been Alloted {0}GB space".format(DriveSize)
      print "<br/>"
      print "Create Partitions and Use"
   else:
      print "Failed Status 1......Contact Support Team"
else:
   print "Failed Status 1......Contact Support Team."

