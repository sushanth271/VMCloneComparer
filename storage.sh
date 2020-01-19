function getDisks()
{
    no_of_disks = $(lsblk | grep disk | wc -l)
    echo "Disks : ${no_of_disks}"
}
function getPartitions()
{
   proc_partitions = $(cat /proc/partitions)
}
getDisks()
getPartitions()
