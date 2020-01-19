function getCPUInfo()
{
    architecture = $(lscpu | grep Architecture | tr -s ' ' | cut -d ' ' -f 2)
    cores = $(cat /proc/cpuinfo | grep processor | wc -l)
    clock = $(lscpu | grep "CPU MHz" | tr -s ' ' | cut -d ' ' -f 3)
    socket = $(lscpu | grep "Socket" | tr -s ' ' | cut -d ' ' -f 2)
    echo "Architecture  ${architecture}"
    echo "No. of processors  ${cores}"
    echo "Clock ${clock}"
    echo "Socket ${socket}"
}
function getMemorySize()
{
    ram = $(cat /proc/meminfo  | grep MemTotal | tr -s ' ' | cut -d ' ' -f 2)
    echo "RAM is ${ram}"
}
function getOs()
{
		
}

getOs()
getCPUInfo()
getMemorySize()

