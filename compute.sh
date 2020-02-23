function getCPUInfo()
{
    architecture=$(lscpu | grep Architecture | tr -s ' ' | cut -d ' ' -f 2)
    cores=$(cat /proc/cpuinfo | grep processor | wc -l)
    clock=$(lscpu | grep "CPU MHz" | tr -s ' ' | cut -d ' ' -f 3)
    sockets=$(lscpu | grep "Socket" | tr -s ' ' | cut -d ' ' -f 2)
    echo "Architecture  ${architecture}"
    echo "No. of processors  ${cores}"
    echo "Clock ${clock}"
    echo "Socket ${sockets}"
}
function getMemorySize()
{
    ram=$(cat /proc/meminfo  | grep MemTotal | tr -s ' ' | cut -d ' ' -f 2)
    echo "RAM is ${ram}"
}
		
cat /proc/sys/kernel/hostname
date

getCPUInfo
getMemorySize

