import subprocess
import sys

def getDiffList(machine1, machine2):
	diffCommand = "ssh " + machine1 + " 'rsync -niad --out-format=%n  /root/ " + machine2 + ":/root/'"
	diffResult1 = subprocess.Popen( diffCommand,stdout=subprocess.PIPE, shell=True)
	diffFiles1 = []
	diffFiles1 = set(diffResult1.stdout.read().splitlines())
	diffCommand = "ssh " + machine2 + " 'rsync -niad --out-format=%n  /root/ " + machine1 + ":/root/'"
	diffResult2 = subprocess.Popen( diffCommand,stdout=subprocess.PIPE, shell=True)
	diffFiles2 = []
	diffFiles2 = set(diffResult2.stdout.read().splitlines())

	return filter(lambda x:  not x.endswith('/') ,list(diffFiles1.union(diffFiles2)))


def compareFSTabEntries(fstab1, fstab2):
	pairs = zip(fstab1, fstab2)
	test = [x for x, y in pairs if x != y]
	test2 = [[(x["device"],k) for k in x if x[k] != y[k]] for x, y in pairs if x != y]
	return test2

def getFSTabEntries(target):
	sshCommand = "ssh " + target + " cat /etc/fstab"
 	fstab = subprocess.Popen( sshCommand ,stdout=subprocess.PIPE, shell=True)
	fstab_ds = []
	for line in fstab.stdout:
		fstab_ds.append(dict(zip(fstab_keys,line.split("\t"))))
	return fstab_ds


diff_result = getDiffList(sys.argv[1], sys.argv[2])
print "----Getting list of files that differ on both VMs.---"
print "\n".join(diff_result)

fstab_keys=["device","mountpoint","fstype","options","backup_opp","fs_check_order"]
fstab1 = getFSTabEntries(sys.argv[1])
fstab2 = getFSTabEntries(sys.argv[2])
print "\n\n----Comparing fstab entries.----"
fstab_result = compareFSTabEntries(fstab1, fstab2)
for i in fstab_result:
	print i[0][1] + " differs for the device :" + i[0][0]

