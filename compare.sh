#!/bin/bash
echo "hi1";
(cat /home/shushanth/Storage.py  | sshpass -p shushanth ssh root@192.168.6.20 python >>abc.txt );	
var1=$(<abc.txt)
echo $var1
	
(cat /home/shushanth/Storage.py  | sshpass -p shushanth ssh root@192.168.6.20 python >>def.txt );	
var2=$(<def.txt)
echo $var2

python /home/shushanth/compare.py var1 var2 >>result.txt
result = $(<result.txt)
echo result
