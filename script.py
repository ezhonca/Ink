import os
print "Hello, Python!"
for dirpath, dirnames, filenames in os.walk('/Users/caizhongming/Desktop/Ink/resource'):
    print 'Directory', dirpath
    for filename in filenames:
        print ' File', filename
