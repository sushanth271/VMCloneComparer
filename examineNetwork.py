import subprocess
import sys

def dict_compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	intersect_keys = d1_keys.intersection(d2_keys)
	d1_notin_d2 = d1_keys - d2_keys
	d2_notin_d1 = d2_keys - d1_keys
	for i in intersect_keys:
		if d1[i] != d2[i] and i != "configuration":
			print "\nParameter: " + str(i) + " machine 1 where as  " + str(d1[i]) + " and machine 2 has " + str(d2[i])
		elif i == "configuration":
			dict_compare(d1[i],d2[i])	
	if len(d1_notin_d2) != 0 :
		print "Machine 1 has the following configurations set where has Machine 2 doesn't." + d1_notin_d2
	
	if len(d2_notin_d1) != 0 :
		print "Machine 2 has the following configurations set where has Machine 1 doesn't." + d2_notin_d1

 	modified = [ (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]]
	same = set(o for o in intersect_keys if d1[o] == d2[o])
	return d1_notin_d2, d2_notin_d1,  modified, same

def processConfig(d1, list1):
	for index,i in enumerate(list1):
		if "=" not in i:
			list1[index-1]+=list1[index]
			list1.pop(index)
	for i in list1:
		i = i.split("=",1)
		d1["configuration"][i[0]] = i[1]

def getNetworkHWInfo(target):
	sshCommand = "ssh " + target + " lshw -class network"
	config = subprocess.Popen( sshCommand ,stdout=subprocess.PIPE, shell=True)
	networkConfiguration = [ x.lstrip(' ') for x in config.stdout.read().splitlines() ]
	dict1 = {}
	for i in networkConfiguration[1:]:
		i = i.split(":",1)
		if( i[0] =="configuration"):
			dict1["configuration"] = {}
			processConfig(dict1, i[1].split())
		else:				
	        	dict1[str(i[0])] = str(i[1])
	return dict1

print "\nComparing network entities:"
dict1 = getNetworkHWInfo(sys.argv[1])
dict2 = getNetworkHWInfo(sys.argv[2])

added, removed, modified, same = dict_compare(dict1, dict2)
print "\nParameteres matched in the two machines are...."
print str(same)
