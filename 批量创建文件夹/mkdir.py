import os, sys
base=''
for i in range(0,100):
    filename = base + str("%04d" % i)
    if os.path.exists(filename):
        pass
    else:
        os.mkdir(filename)
