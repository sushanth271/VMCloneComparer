import subprocess
import sys

def dict_compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	intersect_keys = d1_keys.intersection(d2_keys)
	d1_notin_d2 = d1_keys - d2_keys
	d2_notin_d1 = d2_keys - d1_keys
	for i in intersect_keys:
		if d1[i] != d2[i]:
			print "Parameter: " + str(i) + " machine 1 has " + str(d1[i]) + " and machine 2 has " + str(d2[i])
	if len(d1_notin_d2) != 0 :
		print "Machine 1 has the following configurations set where has Machine 2 doesn't." + d1_notin_d2
	
	if len(d2_notin_d1) != 0 :
		print "Machine 2 has the following configurations set where has Machine 1 doesn't." + d2_notin_d1

 	modified = [ (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]]
	same = set(o for o in intersect_keys if d1[o] == d2[o])
	return d1_notin_d2, d2_notin_d1,  modified, same

def getComputeInfo(target):
	sshCommand = "ssh " + target + " lscpu"
	config = subprocess.Popen( sshCommand ,stdout=subprocess.PIPE, shell=True)
	networkConfiguration = [ x.lstrip(' ') for x in config.stdout.read().splitlines() ]
	dict1 = {}
	for i in networkConfiguration[1:]:
		i = i.split(":",1)
		#if( i[0] =="configuration"):
		#	dict1["configuration"] = {}
		#	processConfig(dict1, i[1].split())
		#else:				
	        dict1[str(i[0])] = str(i[1])
	return dict1

print "Comparing Compute entities:"
dict1 = getComputeInfo(sys.argv[1])
dict2 = getComputeInfo(sys.argv[2])

added, removed, modified, same = dict_compare(dict1, dict2)
print "Parameteres matched in the two machines are...."
print str(same)
