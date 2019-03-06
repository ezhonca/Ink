# -*- coding: utf-8 -*-
import os, json, time, sys, commands, re
reload(sys) 
sys.setdefaultencoding('utf-8')
#print "Hello, Python!"
def printShell(str):
	print '===execute:', str
	(status, output) = commands.getstatusoutput(str)
	print output
printShell('git add *')

print '######begin to create version.json ...'
versionDic = {}
versionDic['version'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
vs = json.dumps(versionDic, ensure_ascii=False)
vf = open('version.json', 'w')
vf.write(vs)
vf.close()
print '######create version.json success'


print '######begin to create update.json ...'
(status, output) = commands.getstatusoutput('git status')
#print output
str = output.decode('utf-8')
#print str
str = "modi a.png modi b.png"


#updateDic['UPDATETIME'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
updateDic = {}
result = re.findall(r"new file:.+resource\/(.+?)\.png", output)

ADDList = []
for s in result:
	sd = s.decode('utf-8')
	(catalog, item) = s.split('/', 1)
	#print catalog, item
	tmpDic = {}
	tmpDic['catalog'] = catalog.decode('utf-8')
	tmpDic['item'] = item.decode('utf-8')
	ADDList.append(tmpDic)
updateDic['ADD'] = ADDList
#print updateDic

deleresult = re.findall(r"deleted:.+resource\/(.+?)\.png", output)
DELEList = []
for s in deleresult:
	sd = s.decode('utf-8')
	(catalog, item) = s.split('/', 1)
	#print catalog, item
	tmpDic = {}
	tmpDic['catalog'] = catalog.decode('utf-8')
	tmpDic['item'] = item.decode('utf-8')
	DELEList.append(tmpDic)
updateDic['DELETE'] = DELEList
#print updateDic

MODIResult = re.findall(r"modified:.+resource\/(.+?)\.png", output)
MODIList = []
for s in MODIResult:
	sd = s.decode('utf-8')
	(catalog, item) = s.split('/', 1)
	#print catalog, item
	tmpDic = {}
	tmpDic['catalog'] = catalog.decode('utf-8')
	tmpDic['item'] = item.decode('utf-8')
	MODIList.append(tmpDic)
updateDic['MODIFIED'] = MODIList
#print updateDic
res = json.dumps(updateDic, ensure_ascii=False)
#print re
uf = open('update.json', 'w')
uf.write(res)
uf.close()
print '######create update.json success'
printShell('cat update.json')




print '######begin to create resource.json ...'
dic = {}
for dirpath, dirnames, filenames in os.walk('/Users/caizhongming/Desktop/Ink/resource'):
    
    if dirpath != '/Users/caizhongming/Desktop/Ink/resource':
    	list = [];
    	#print 'Directory', dirpath
    	fn = dirpath.replace('/Users/caizhongming/Desktop/Ink/resource/','').decode('utf-8')
    	#print fn

    	#f = open('resource.json', 'w')
    	#f.write(fn)
    	#f.close()
        
    	for filename in filenames:
    		name = re.findall(r"(.+?)\.png", filename)
    		for n in name:
        	#print ' File', filename
        		if n:
        			list.append(n)
        dic[fn] = list
#print dic
json = json.dumps(dic, ensure_ascii=False)
#print json
f = open('resource.json', 'w')
f.write(json)
f.close()
print '######create resource.json success'
printShell('cat resource.json')

printShell('git add *')
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
printShell('git commit -m \'' + t + '\'')
printShell('git push -u origin master')
#print result
#json = json.dumps(result, ensure_ascii=False)
#print json










