# VMCloneComparer
Provision to compare network,storage,compute of 2 VMs. 
Output:
[root@mb-centos69x64-01 VMCloneComparer]# ./examineVm.sh root@172.16.41.90 root@172.16.41.152
Comparing Network Parameters of the two VMs
Comparing network entities:
Parameter: serial machine 1 has  00:50:56:a6:dd:e5 and machine 2 has  00:50:56:a6:50:f5
Parameter: ip machine 1 has 172.16.41.90 and machine 2 has 172.16.41.152

Parameteres matched in the two machines are....
set(['product', 'vendor', 'description', 'clock', 'logical name', 'bus info', 'width', 'version', 'capabilities', 'physical id', 'resources', 'size'])

Comparing Compute Parameters of the two VMs
Comparing Compute entities:

Parameteres matched in the two machines are....
set(['CPU(s)', 'L1d cache', 'CPU op-mode(s)', 'NUMA node0 CPU(s)', 'Hypervisor vendor', 'L2 cache', 'L1i cache', 'Model name', 'CPU MHz', 'Core(s) per socket', 'Virtualization type', 'Thread(s) per core', 'On-line CPU(s) list', 'Socket(s)', 'Model', 'Vendor ID', 'CPU family', 'L3 cache', 'BogoMIPS', 'Stepping', 'Byte Order', 'NUMA node(s)'])
