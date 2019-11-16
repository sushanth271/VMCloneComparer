import os
import stat
import json
import re
ms = {}
dirss = set()
dirkey = ()
symlinks = []
for dirpath, dirnames, filenames in os.walk('/home/sushanth/Desktop',topdown = False, followlinks = True):
    if re.match("/proc*",dirpath) or re.match("/var/run*",dirpath):
	#print "not traversing"
	#print dirpath
        continue
   # print dirpath
   # print dirnames
   # print filenames
    for i in filenames:
        ms[dirpath+'/'+i] = []
        ms[dirpath+'/'+i].append("Path: "+dirpath+'/'+i)
        ms[dirpath+'/'+i].append("Inode Protection Mode: "+str(os.stat(dirpath+'/'+i).st_mode))
        ms[dirpath+'/'+i].append("Inode number: "+str(os.stat(dirpath+'/'+i).st_ino))
        ms[dirpath+'/'+i].append("Device inode resides on: "+str(os.stat(dirpath+'/'+i).st_dev))
        ms[dirpath+'/'+i].append("Number of links to the inode: "+str(os.stat(dirpath+'/'+i).st_nlink))
        ms[dirpath+'/'+i].append("User id of the owner: "+str(os.stat(dirpath+'/'+i).st_uid))
        ms[dirpath+'/'+i].append("Group id of the owner: "+str(os.stat(dirpath+'/'+i).st_gid))
        ms[dirpath+'/'+i].append("Size in bytes: "+str(os.stat(dirpath+'/'+i).st_size))
        ms[dirpath+'/'+i].append("Time of last access: "+str(os.stat(dirpath+'/'+i).st_atime))
        ms[dirpath+'/'+i].append("Time of last modification: "+str(os.stat(dirpath+'/'+i).st_mtime))
        ms[dirpath+'/'+i].append("Creation time: "+str(os.stat(dirpath+'/'+i).st_ctime))
        ms[dirpath+'/'+i].append("File")
    ms[dirpath] = []
    ms[dirpath].append("Path: "+dirpath)
    ms[dirpath].append("Inode Protection Mode: "+str(os.stat(dirpath).st_mode))
    ms[dirpath].append("Inode number: "+str(os.stat(dirpath).st_ino))
    ms[dirpath].append("Device inode resides on: "+str(os.stat(dirpath).st_dev))
    ms[dirpath].append("Number of links to the inode: "+str(os.stat(dirpath).st_nlink))
    ms[dirpath].append("User id of the owner: "+str(os.stat(dirpath).st_uid))
    ms[dirpath].append("Group id of the owner: "+str(os.stat(dirpath).st_gid))
    ms[dirpath].append("Size in bytes: "+str(os.stat(dirpath).st_size))
    ms[dirpath].append("Time of last access: "+str(os.stat(dirpath).st_atime))
    ms[dirpath].append("Time of last modification: "+str(os.stat(dirpath).st_mtime))
    ms[dirpath].append("Creation time: "+str(os.stat(dirpath).st_ctime))
    ms[dirpath].append("Folder")
    ms[dirpath].append({})
    ms[dirpath].append({})
    for i in dirnames:
         ms[dirpath][12][i]=ms[dirpath+'/'+i]
         ms[dirpath+'/'+i]       
         ms[dirpath][12][i]=ms[dirpath+'/'+i]
         #print ms[dirpath +'/' +i]
    for i in filenames:
        ms[dirpath][13][i]=ms[dirpath+'/'+i]
        ms[dirpath+'/'+i]
#print ms
#print ms['/proc/asound/I82801AAICH']
print ms
#msjson = json.dumps(ms)
#print json.dumps(ms['/home/sushanth/Desktop'], sort_keys=True, indent=4)



def details(path):
    indexpath = ''
    twelve = 12
    msout = ms['/home/shushanth/Desktop/RackWare Internship']
    print path
    path = path[43:]
    pathsplit = path.split('/')
    for i in pathsplit[1:]:
        indexpath = indexpath + '[' + `twelve` + ']' + "[" + i + "]"
    print indexpath
    indexpath = indexpath[1:-1]
    indexlist = indexpath.split('][')
    msoutdict = {}
    print indexlist
    for i in indexlist:
        if i == '12':
            #print "MSOUTDICT--------"
            #print msoutdict
            msoutdict = msout[int(i)]
        else:
            #print "MSOUT---------"
            #print msout
            msout = msoutdict[str(i)]
    return msout
    #print msout
    #print ms['/home/shushanth/Desktop/RackWare Internship'][11][indexpath]

def details_file(path):
    indexpath = ''
    twelve = 12
    thirteen = 13
    msout = ms['/home/shushanth/Desktop/RackWare Internship']
    print path
    path = path[43:]
    pathsplit = path.split('/')
    count = len(pathsplit)
    x = 0
    for index,i in enumerate(pathsplit[1:]):
        if index!=count-2:
            indexpath = indexpath + '[' + `twelve` + ']' + "[" + i + "]"
        else:
            indexpath = indexpath + '[' + `thirteen` + ']' + "[" + i + "]"
    print indexpath
    indexpath = indexpath[1:-1]
    indexlist = indexpath.split('][')
    msoutdict = {}
    print indexlist
    for i in indexlist:
        if i == '12' or i == '13':
            #print "MSOUTDICT--------"
            #print msoutdict
            msoutdict = msout[int(i)]
        else:
            #print "MSOUT---------"
            #print msout
            msout = msoutdict[str(i)]
    return msout
