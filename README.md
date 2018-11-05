# SummerInternship2017-LinuxWorld Informatics pvt. ltd. Jaipur
Cloud Computing

It is a cloud prototype with various major services such as Storage as a service(Staas) , Software as a service(Saas) ,
Container as a Service(Caas) ,Platform as a Service(Paas) and Infrastructure as a Service(Iaas). The Code was tested and Developed on
Redhat Operating System.

#Storage as a Service(Staas)
It is providing storage over the Network to the user. It is of two types :-
a> Object Storage :- Object storage is a computer data storage architecture that manages data as objects,
as opposed to other storage architectures like file systems which manage data as a file hierarchy, and block storage 
which manages data as blocks within sectors and tracks. We have used Network File System(NFS) protocol to share storage on the network.
The Object Storage is used for storing files such as video ,texts etc.

b> Block Storage :- In Blocks Storage the whole device get shared across the network. It allows user to create its own partition.
The Protocol used is iscsi protocol.

The Storage Created and shared was on logical volumes. The major features were storing file across the network, extending the storage allocated
creating a snapshot of the current state.

#Platform as a Service(Paas)
Platform as a Service (PaaS) or Application Platform as a Service (aPaaS) or platform base service is a category of cloud computing services 
that provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining 
the infrastructure typically associated with developing and launching an app. Here We have provided Bash Shell using HTML textbox by
redirecting the input to the shell.

#Software as a Service
Software as a service (SaaS) is a software distribution model in which a third-party provider hosts applications and makes them available 
to customers over the Internet. We used mozilla firefox of a remote computer through SSH Protocol and X11 forwarding. This allows user to use 
software installed on other systems without a need for installing it.

#Container as a Service
Container as a service we used container technology to launch containers here we used docker. Containers allow us to launch a environment that is 
suitable for installing software. It is fast and secure. We can launch a new os within seconds. We created a management portal to
launc hmultiple containers , manage all the running containers and creating docker images as per the needs.

#Infrastructure as a Service
It is launching a os in virtualized environment on server side then sharing its shell over network. We provided various options such as
selecting ram, OS, storage etc. It is like buying a new system. In future according to needs ram and storage could be increased. This 
service allows user to use or control the system over the network. Now user can use this system as per its requirements install the software
as per needs. The user needs internet only to access the shell. The internet of cloud provider will be used to download new softwares.

#DevOps
We have used a DevOps tool- Ansible to automate our tasks. For example, In storage as a service we need to create partitions, setup volume
groups, logical volumes, format the partitions, mounting the partitons and update the entries in configurations file. This all tasks are
done using ansible tool.

TECHNOLOGIES USED
>> Docker(Container Technology).
>> Ansible(DevOps Tool).
>> Operating System: Redhat.
>> Backend Technology - Python CGI integration with HTML.
>> FrontEnd Technology - HTML,CSS.
>>Scripting - Python. 
