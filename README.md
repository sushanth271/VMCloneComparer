# VMCloneComparer
Provision to compare network,storage,compute of 2 VMs. 

Output:
[root@mb-centos69x64-01 VMCloneComparer]# ./examineVm.sh root@172.16.41.90 root@172.16.41.152

Comparing storage entities.
Getting list of files that differ on both VMs.
.ssh/known_hosts
.ssh/id_rsa.pub
.ssh/id_rsa
.bash_history
.viminfo
test5/test6/test2
test5/test6/test3
test5/test1
.ssh/authorized_keys


Comparing fstab entries.
mountpoint differs for the device :devpts

Comparing network entities:

Parameter: serial machine 1 where as   00:50:56:a6:dd:e5 and machine 2 has  00:50:56:a6:50:f5

Parameter: ip machine 1 where as  172.16.41.90 and machine 2 has 172.16.41.152

Parameteres matched in the two machines are....
set(['product', 'vendor', 'description', 'clock', 'logical name', 'bus info', 'width', 'version', 'capabilities', 'physical id', 'resources', 'size'])

Comparing Compute entities:

Parameteres matched in the two machines are....
set(['CPU(s)', 'L1d cache', 'CPU op-mode(s)', 'NUMA node0 CPU(s)', 'Hypervisor vendor', 'L2 cache', 'L1i cache', 'Model name', 'CPU MHz', 'Core(s) per socket', 'Virtualization type', 'Thread(s) per core', 'On-line CPU(s) list', 'Socket(s)', 'Model', 'Vendor ID', 'CPU family', 'L3 cache', 'BogoMIPS', 'Stepping', 'Byte Order', 'NUMA node(s)'])
[root@mb-centos69x64-01 VMCloneComparer]#
