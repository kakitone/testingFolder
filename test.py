import os
print "hi3"
assert(1==1)
f = open("localitem.txt", 'w')
f.write('1')
f.close()

f=open("localitem.txt", 'r')
tmp = f.readline().rstrip()
assert(tmp == '1')
print "tmp: "+ tmp
f.close()

os.system("wget https://www.dropbox.com/s/rzkd0op81rj6my1/download.txt?dl=1 -O /tmp/dow")
f=open("/tmp/dow", 'r')
tmp = f.readline().rstrip()
assert(tmp =='2')
print "tmp2: "+ tmp
f.close()


